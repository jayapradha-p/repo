from __future__ import annotations

import asyncio
import datetime
import uuid
from typing import Any

from SiemplifyConnectorsDataModel import AlertInfo
from SiemplifyUtils import convert_string_to_unix_time, utc_now
from TIPCommon.extraction import extract_connector_param
from TIPCommon.consts import NUM_OF_MILLI_IN_SEC, NUM_OF_SEC_IN_MIN
from TIPCommon.filters import filter_old_alerts, pass_whitelist_filter
from TIPCommon.transformation import dict_to_flat
from TIPCommon.smp_time import unix_now
from TIPCommon.base.connector.async_connector import AsyncConnector

import constants
from datamodels import Incident, IncidentAlert, IncidentProperties
from exceptions import (
    MicrosoftAzureSentinelError,
    TimeoutIsApproachingError,
    MicrosoftAzureSentinelIncidentNotFoundError,
)
from MicrosoftAzureSentinelCommon import (
    create_regular_alert_events,
    create_scheduled_alert_events,
    MicrosoftAzureSentinelCommon,
    read_backlog_ids,
    read_next_page_alerts,
    write_backlog_ids,
    write_next_page_alerts,
)
from MicrosoftAzureSentinelAsyncManager import MicrosoftAzureSentinelAsyncManager
from MicrosoftAzureSentinelParser import MicrosoftAzureSentinelParser
from utils import (
    convert_hours_to_milliseconds,
    dict_to_md5_hash,
    get_chunks_as_context_property,
    get_value_from_template,
    find_fallback_value,
    set_chunks_as_context_property,
    split_dict_into_chunks,
)


class IncidentTrackingConnector(AsyncConnector):
    def __init__(self) -> None:
        super().__init__(script_name=constants.INCIDENT_TRACKING_CONNECTOR_NAME)
        self.coros_limit = constants.COROS_LIMIT
        self.manager: MicrosoftAzureSentinelAsyncManager | None = None
        self.sentinel_common = MicrosoftAzureSentinelCommon(self.logger)
        self.processed_items = {}

    def extract_params(self) -> None:
        """Extract action parameters and populate them into .params container."""
        super().extract_params()

        self.params.use_same_approach = extract_connector_param(
            self.siemplify,
            param_name=(
                "Use the same approach with event creation for all alert types?"
            ),
            input_type=bool,
            print_value=True,
        )
        self.params.alerts_for_no_entities = extract_connector_param(
            self.siemplify,
            param_name=(
                "Create Chronicle SOAR Alerts for Sentinel incidents that do "
                "not have entities?"
            ),
            input_type=bool,
            print_value=True,
        )
        self.params.fallback_logic_debug = extract_connector_param(
            self.siemplify,
            param_name="Enable Fallback Logic Debug?",
            input_type=bool,
            print_value=True,
        )

        self.params.incidents_padding_period = extract_connector_param(
            self.siemplify,
            param_name="Incidents Padding Period (minutes)",
            input_type=int,
            print_value=True,
            default_value=0,
        )
        self.params.incidents_tracking_hours = extract_connector_param(
            self.siemplify,
            param_name="How many hours to track ingested incident for updates",
            is_mandatory=True,
            input_type=int,
            print_value=True,
            default_value=constants.INCIDENTS_TRACKING_DEFAULT_HOURS,
        )
        self.params.scheduled_alerts_events_limit_to_ingest = extract_connector_param(
            self.siemplify,
            param_name="Total number of Scheduled Alerts Events Limit to Ingest",
            input_type=int,
            print_value=True,
        )
        self.params.wait_for_scheduled_alerts = extract_connector_param(
            self.siemplify,
            param_name="Wait For Scheduled/NRT Alert Object",
            input_type=bool,
            print_value=True,
            default_value=False
        )

    def validate_params(self) -> None:
        """Validate connector parameters."""
        self.params.max_incidents_per_cycle = self.param_validator.validate_positive(
            param_name="Max Incidents per Cycle",
            value=self.params.max_incidents_per_cycle,
        )
        self.params.max_backlog_incidents_per_cycle = (
            self.param_validator.validate_positive(
                param_name="Max Backlog Incidents per cycle",
                value=self.params.max_backlog_incidents_per_cycle,
            )
        )
        self.params.max_hours_backwards = self.param_validator.validate_positive(
            param_name="Max Hours Backwards", value=self.params.max_hours_backwards
        )
        self.params.scheduled_alerts_events_limit_to_ingest = (
            self.param_validator.validate_positive(
                param_name="Total number of Scheduled Alerts Events Limit to Ingest",
                value=self.params.scheduled_alerts_events_limit_to_ingest,
            )
        )
        self.params.backlog_expiration_timer = self.param_validator.validate_positive(
            param_name="Backlog Expiration Timer",
            value=self.params.backlog_expiration_timer,
        )
        if self.params.incidents_padding_period is not None:
            self.params.incidents_padding_period = (
                self.param_validator.validate_non_negative(
                    param_name="Incidents Padding Period (minutes)",
                    value=self.params.incidents_padding_period,
                )
            )

        self.params.incident_statuses_to_fetch = self.param_validator.validate_csv(
            param_name="Incident Statuses to Fetch",
            csv_string=self.params.incident_statuses_to_fetch,
        )
        self.params.incidents_tags_to_ingest = self.param_validator.validate_csv(
            param_name="Incidents Tags To Ingest",
            csv_string=self.params.incidents_tags_to_ingest,
        )
        self.params.incident_severities_to_fetch = self.param_validator.validate_csv(
            param_name="Incident Severities to Fetch",
            csv_string=self.params.incident_severities_to_fetch,
        )
        self.params.start_time_fallback = self.param_validator.validate_csv(
            param_name="StartTimeFallback", csv_string=self.params.start_time_fallback
        )
        self.params.end_time_fallback = self.param_validator.validate_csv(
            param_name="EndTimeFallback", csv_string=self.params.end_time_fallback
        )
        self.params.product_field_fallback = self.param_validator.validate_csv(
            param_name="ProductFieldFallback",
            csv_string=self.params.product_field_fallback,
        )
        self.params.vendor_field_fallback = self.param_validator.validate_csv(
            param_name="VendorFieldFallback",
            csv_string=self.params.vendor_field_fallback,
        )
        self.params.event_field_fallback = self.param_validator.validate_csv(
            param_name="EventFieldFallback", csv_string=self.params.event_field_fallback
        )
        self.params.incidents_tracking_hours = self.param_validator.validate_positive(
            param_name="How many hours to track ingested incident for updates",
            value=self.params.incidents_tracking_hours,
        )

    def init_managers(self) -> None:
        self.manager = MicrosoftAzureSentinelAsyncManager(
            api_root=self.params.api_root,
            client_id=self.params.client_id,
            client_secret=self.params.client_secret,
            tenant_id=self.params.entra_id_directory_id,
            workspace_id=self.params.azure_sentinel_workspace_name,
            resource=self.params.azure_resource_group,
            subscription_id=self.params.azure_subscription_id,
            login_url=self.params.oauth2_login_endpoint_url,
            verify_ssl=self.params.verify_ssl,
            siemplify=self.siemplify,
        )

    def get_last_success_time(self, *_) -> datetime.datetime:
        """Get last_success_time for connector from DB (or FileStorage)."""
        return super().get_last_success_time(
            max_backwards_param_name="max_hours_backwards",
            metric="hours",
            padding_period_param_name="incidents_padding_period",
            padding_period_metric="minutes",
        )

    def read_context_data(self) -> None:
        """Read connector's context data from DB (or FileStorage)."""
        self.logger.info("Reading already existing alerts ids...")
        self.context.existing_ids = get_chunks_as_context_property(
            self.siemplify, constants.IDS_KEY
        )
        self.context.expired_existing_ids = self._get_expired_existing_ids()
        self.context.backlog_ids = read_backlog_ids(self.siemplify)
        self.context.initial_backlog = set(self.context.backlog_ids)
        self.context.next_page_link = read_next_page_alerts(self.siemplify)

    def _get_expired_existing_ids(self) -> list[str]:
        """
        Get expired existing incident ids

        Returns:
            [str]: list of expired incident ids
        """
        tracking_ms = convert_hours_to_milliseconds(
            self.params.incidents_tracking_hours
        )

        return [
            key
            for key, value in self.context.existing_ids.items()
            if value.get("ingested_time", 0) + tracking_ms <= self.connector_start_time
        ]

    def store_alert_in_cache(self, incident: Incident) -> None:
        """Store alert in connector's IDs cache.

        Args:
            incident: Incident's data model

        Returns:
            None, updates self.context.existing_ids with incident.name
        """
        self.processed_items[incident.name] = self._collect_seen_ids(
            incident, self.context.existing_ids.get(incident.name)
        )

        self.context.existing_ids.update(
            {incident.name: self.processed_items[incident.name]}
        )

    def is_overflow_alert(self, alert_info: AlertInfo) -> bool:
        return not self.params.disable_overflow and super().is_overflow_alert(
            alert_info
        )

    def set_last_success_time(
        self, filtered_alerts: list[Incident], unprocessed_alerts: list[Incident], *_
    ) -> None:
        """Saves last_success_time into DB (or FileStorage)."""

        def after_last_success_time(inc: Incident) -> bool:
            return (
                inc.last_modified_time_ts
                > self.context.last_success_timestamp.timestamp() * NUM_OF_MILLI_IN_SEC
            )

        super().set_last_success_time(
            filtered_alerts=list(filter(after_last_success_time, filtered_alerts)),
            unprocessed_alerts=list(
                filter(after_last_success_time, unprocessed_alerts)
            ),
            timestamp_key="last_modified_time_ts",
        )

    def write_context_data(self, filtered_alerts: list[Incident], _: Any) -> None:
        """Saves connector's context data into DB (or FileStorage)."""
        if filtered_alerts:
            self._exclude_expired_data_from_existing_ids()
            self.logger.info("Saving existing ids.")
            set_chunks_as_context_property(
                self.siemplify,
                constants.IDS_KEY,
                split_dict_into_chunks(self.context.existing_ids),
            )

            self._exclude_fetched_alerts_from_backlog(filtered_alerts)

        if self.context.initial_backlog.symmetric_difference(self.context.backlog_ids):
            self.logger.info("Saving backlog ids.")
            write_backlog_ids(self.siemplify, self.context.backlog_ids)

    def _exclude_expired_data_from_existing_ids(self):
        """
        Exclude expired data from existing ids
        """
        for incident_id, values in self.context.existing_ids.items():
            if incident_id in self.context.expired_existing_ids:
                values.pop("alerts", None)

    def _exclude_fetched_alerts_from_backlog(self, fetched_alerts: list[Incident]):
        """
        Exclude from backlog fetched alerts that were already processed
        Args:
            fetched_alerts (list[Incident]): list of fetched alerts
        """
        incident_number_lookup = {
            str(incident.properties.incident_number)
            for incident in fetched_alerts
            if incident.name in self.context.existing_ids.keys()
        }

        if incident_number_lookup:
            self.context.next_page_link = ""

        self.context.backlog_ids = {
            id_: ts
            for id_, ts in self.context.backlog_ids.items()
            if id_ not in incident_number_lookup
        }

    async def finalize(self) -> None:
        """Connector finalization coroutine."""
        if not hasattr(self.context, "next_page_link"):
            return

        write_next_page_alerts(
            self.siemplify, data_to_write=self.context.next_page_link
        )

        if self.manager is not None:
            await self.manager.async_client.aclose()

    async def _get_backlog_incidents(self) -> list[Incident]:
        """Fetch backlog incidents data from Azure Sentinel.

        Returns:
            List of Incident data models
        """
        fetched_backlog_incidents = []

        backlog_incidents_futures = [
            self.manager.get_incident_by_number(incident_number=inc_number)
            for inc_number in self.context.backlog_ids
        ]

        for backlog_incident_future in asyncio.as_completed(backlog_incidents_futures):
            try:
                self.sentinel_common.raise_if_timeout(
                    self.connector_start_time,
                    self.params.python_process_timeout,
                    constants.FETCH_TIMEOUT_THRESHOLD,
                )

                if (
                    len(fetched_backlog_incidents)
                    >= self.params.max_backlog_incidents_per_cycle
                ):
                    self.logger.info(
                        "Limit of backlog id's to process per cycle is reached, "
                        "exiting ..."
                    )
                    break

                fetched_backlog_incidents.append(await backlog_incident_future)

            except TimeoutIsApproachingError as error:
                self.logger.info(str(error))
                break
            except MicrosoftAzureSentinelIncidentNotFoundError as error:
                inc_number, error_msg = error.args
                self.logger.error(
                    f"Failed to fetch {inc_number} backlog incident. Error: {error_msg}"
                )

        return fetched_backlog_incidents

    async def get_alerts(self) -> list[Incident]:
        """Fetches new incidents from Azure Sentinel.

        Returns:
            List of Incident data models
        """
        fetched_backlog_incidents = await self._get_backlog_incidents()
        self.logger.info(f"Fetched {len(fetched_backlog_incidents)} backlog alerts.")

        filtered_incidents_lookup = set(self.context.expired_existing_ids)
        filtered_incidents_lookup.update(
            incident.name for incident in fetched_backlog_incidents
        )

        try:
            (
                fetched_incidents,
                self.context.next_page_link,
            ) = await self.manager.get_incidents_with_new_endpoint(
                updated_time=self.context.last_success_timestamp,
                statuses=self.params.incident_statuses_to_fetch,
                severities=self.params.incident_severities_to_fetch,
                limit=self.params.max_incidents_per_cycle,
                existing_ids=filtered_incidents_lookup,
                next_page_link=self.context.next_page_link,
            )
        except MicrosoftAzureSentinelError:
            self.context.next_page_link = ""
            raise

        self.logger.info(f"Number of fetched alerts: {len(fetched_incidents)}")

        fetched_incidents.extend(fetched_backlog_incidents)
        self.logger.info(f"Total alerts to process: {len(fetched_incidents)}")
        return fetched_incidents

    def filter_alerts(self, alerts: list[Incident]) -> list[Incident]:
        """Filter fetched incidents to exclude already fetched.

        Args:
            alerts: List of Incident data models

        Returns:
            List of filtered Incident data models sorted by last_modified_time_ts
        """
        return sorted(
            filter_old_alerts(
                self.siemplify,
                alerts=alerts,
                existing_ids=self.context.expired_existing_ids,
                id_key="name",
            ),
            key=lambda _alert: _alert.last_modified_time_ts,
        )

    async def process_alert(self, alert: Incident) -> Incident:
        """Process alert coroutine."""
        self.logger.info(
            f"Processing incident {alert.alert_id} "
            f"with timestamps: {alert.last_modified_time_ts}"
        )

        return await self.manager.adjust_incidents_alerts_data(
            incident=alert,
            connector_starting_time=self.connector_start_time,
            python_process_timeout=self.params.python_process_timeout,
            scheduled_alerts_events_limit=(
                self.params.scheduled_alerts_events_limit_to_ingest
            ),
            scheduled_alerts_new_events_limit=(
                (
                    self.params.scheduled_alerts_events_limit_to_ingest
                    - self._calculate_existing_scheduled_alerts_events(alert)
                )
                if self.params.scheduled_alerts_events_limit_to_ingest
                else None
            ),
            incidents_alerts_limit_to_ingest=None,
            backlog_ids=self.context.backlog_ids,
            alerts_for_no_entities=self.params.alerts_for_no_entities,
            use_same_approach=self.params.use_same_approach,
            incident_existing_items=(self.context.existing_ids.get(alert.name, {})),
            wait_for_scheduled_alerts=self.params.wait_for_scheduled_alerts,
        )

    def pass_filters(self, alert: Incident) -> bool:
        """Check if incident passes filters and is fully fetched.

        Args:
            alert (Incident): Incident data model

        Returns:
            bool: True if passes filter, False otherwise
        """
        _incident_number = str(alert.properties.incident_number)

        if self._reached_scheduled_alerts_events_limit(alert):
            self.logger.info(
                f"Alert {alert.name} ({_incident_number}) reached total number of "
                f"events limit to ingest. Skipping..."
            )
            return False

        if self._already_seen_items(alert):
            self.logger.info(
                f"Alert {alert.name} ({_incident_number}) with all related items "
                f"has already been seen. Skipping..."
            )
            return False

        return (
            self._pass_dynamic_list_filter_and_adjust_backlog(alert, _incident_number)
            and self._pass_tags_filter_and_adjust_backlog(alert, _incident_number)
            and self._pass_backlog_filter_and_adjust_backlog(alert, _incident_number)
        )

    def _pass_dynamic_list_filter_and_adjust_backlog(
        self, alert: Incident, incident_number: str
    ) -> bool:
        """
        Check if incident passes dynamic list filter and adjust backlog based on filter

        Args:
            alert (Incident): Incident data model
            incident_number (str): Incident number

        Returns:
            bool: True if passes dynamic list filter, False otherwise
        """
        if self.siemplify.whitelist and not pass_whitelist_filter(
            siemplify=self.siemplify,
            whitelist_as_a_blacklist=self.params.use_dynamic_list_as_a_blocklist,
            model=alert,
            model_key="incident_title",
        ):
            if incident_number in self.context.backlog_ids:
                self.logger.info(
                    f"Backlog alert {alert.name} ({incident_number}) "
                    "is blacklisted, removing from backlog ..."
                )
                del self.context.backlog_ids[incident_number]

            return False

        return True

    def _pass_tags_filter_and_adjust_backlog(
        self, alert: Incident, incident_number: str
    ) -> bool:
        """
        Check if incident passes tags filter and adjust backlog based on filter

        Args:
            alert (Incident): Incident data model
            incident_number (str): Incident number

        Returns:
            bool: True if passes tags filter, False otherwise
        """
        if self.params.incidents_tags_to_ingest and not (
            alert.incident_labels
            and pass_whitelist_filter(
                self.siemplify,
                whitelist_as_a_blacklist=False,
                model=alert,
                model_key="incident_labels",
                whitelist=self.params.incidents_tags_to_ingest,
            )
        ):
            if incident_number in self.context.backlog_ids:
                self.logger.info(
                    f"Backlog alert {alert.name} ({incident_number}) "
                    "is blacklisted by tags, removing from backlog ..."
                )
                del self.context.backlog_ids[incident_number]

            return False

        return True

    def _pass_backlog_filter_and_adjust_backlog(
        self, alert: Incident, incident_number: str
    ) -> bool:
        """
        Check if incident passes backlog filter and adjust backlog based on filter

        Args:
            alert (Incident): Incident data model
            incident_number (str): Incident number

        Returns:
            bool: True if passes backlog filter, False otherwise
        """
        if alert.fully_fetched:
            _processing_type = (
                "Backlog alert"
                if incident_number in self.context.backlog_ids
                else "Regular alert"
            )
            self.logger.info(
                f"{_processing_type} {alert.name} ({incident_number})"
                f" will be fully processed"
            )

        elif incident_number not in self.context.backlog_ids:
            self.logger.info(
                f"Sending alert {alert.name} ({incident_number}) to backlog."
            )
            self.context.backlog_ids[incident_number] = unix_now()
            return False

        elif self._is_backlog_incident_expired(incident_number):
            self.logger.info(
                f"Expired backlog alert "
                f"{alert.name} ({incident_number}) will be "
                f"partially processed."
            )

        else:
            self.logger.info(
                f"Alert {alert.name} ({incident_number}) will stay "
                f"in backlog as it wasn't fully fetched."
            )
            return False

        return True

    def _set_time_for_alert(
        self, alert_info: AlertInfo, incident: Incident, flat_incident: dict[str, str]
    ) -> None:
        """Try setting start and end time using fallbacks and log the process.

        Args:
            alert_info: AlertInfo object of SOAR alert
            incident: Incident data model
            flat_incident: Flat incident data to use for fallbacks fetch

        Returns:
            None, update alert_info on the spot
        """
        alert_info.start_time = self._get_alert_time_value(
            incident=incident,
            flat_incident=flat_incident,
            fallback_keys=self.params.start_time_fallback,
            fallback_logic_debug_key="StartTimeFallback",
            alert_time_key_name="start time",
        )

        alert_info.end_time = self._get_alert_time_value(
            incident=incident,
            flat_incident=flat_incident,
            fallback_keys=self.params.end_time_fallback,
            fallback_logic_debug_key="EndTimeFallback",
            alert_time_key_name="end time",
        )

    def _get_alert_time_value(
        self,
        incident: Incident,
        flat_incident: dict[str, str],
        fallback_keys: [str],
        fallback_logic_debug_key: str,
        alert_time_key_name: str,
    ) -> int:
        """
        Get alert time value
        Args:
            incident (Incident): Incident data model
            flat_incident (dict[str, str]): flat incident data
            fallback_keys ([str]): list of keys to use for value extraction
            fallback_logic_debug_key (str): key to set for fallback logic debug
            alert_time_key_name (str): alert time key name

        Returns:
            int: alert time value in unix format
        """
        fallback = (
            self._get_fallback_value(
                flat_incident, fallback_keys, fallback_logic_debug_key
            )
            or incident.properties.created_time_utc
        )

        if fallback:
            alert_time = convert_string_to_unix_time(fallback)
            if self.params.fallback_logic_debug and not flat_incident.get(
                fallback_logic_debug_key
            ):
                flat_incident[fallback_logic_debug_key] = "CreatedTimeUTC"
        else:
            alert_time = unix_now()
            self.logger.info(
                f"Chronicle SOAR Alert's {alert_time_key_name} is set to current time,"
                f" as no values were found with the provided fallback fields."
            )
            if self.params.fallback_logic_debug:
                flat_incident[fallback_logic_debug_key] = "Current time"

        return alert_time

    def _set_product_and_vendor_for_alert(
        self, alert_info: AlertInfo, incident: Incident, flat_incident: dict[str, str]
    ) -> None:
        """Try setting Vendor and Product using fallbacks and log the process.

        Args:
            alert_info: AlertInfo object of SOAR alert
            incident: Incident data model
            flat_incident: Flat incident data to use for fallbacks fetch

        Returns:
            None, update alert_info on the spot
        """
        product_value = self._get_fallback_value(
            flat_incident, self.params.product_field_fallback, "ProductFieldFallback"
        )

        vendor_value = self._get_fallback_value(
            flat_incident, self.params.vendor_field_fallback, "VendorFieldFallback"
        )

        if incident.properties.alerts:
            source_alert: IncidentAlert = incident.properties.alerts[0]
            vendor_value = (
                source_alert.scheduled_alert.vendor_name
                if source_alert.scheduled_alert is not None
                else source_alert.properties.vendor_name
            )
            flat_events = (
                source_alert.scheduled_alert.get_events_flat()
                if source_alert.scheduled_alert is not None
                else []
            )
            source_event_flat = flat_events[0] if flat_events else {}

            product_value, _ = find_fallback_value(
                source_dicts=[
                    source_event_flat,
                    dict_to_flat(source_alert.to_event()),
                    flat_incident,
                ],
                fallbacks_list=self.params.product_field_fallback,
            )

        alert_info.device_vendor = (
            vendor_value if vendor_value else constants.DEFAULT_VENDOR_NAME
        )
        alert_info.device_product = (
            product_value if product_value else constants.DEFAULT_PRODUCT_NAME
        )

    def _get_fallback_value(
        self, data: dict, fallback_keys: [str], fallback_logic_debug_key: str
    ) -> str | None:
        """
        Get fallback value from provided data
        Args:
            data (dict): data to extract fallback value from
            fallback_keys ([str]): list of keys to use for value extraction
            fallback_logic_debug_key (str): key to set for fallback logic debug

        Returns:
            str | None: fallback value or None
        """
        fallback_value = None

        for fallback_key in fallback_keys:
            fallback_value = data.get(fallback_key)
            if fallback_value:
                if self.params.fallback_logic_debug:
                    data[fallback_logic_debug_key] = fallback_key
                break

        return fallback_value

    def _build_events_data(
        self, incident: Incident, flat_incident: dict[str, str]
    ) -> list[dict[str, str]]:
        """Build events data out of alerts for incident and return their flat data.

        Args:
            incident (Incident): Incident data model
            flat_incident (dict[str, str]): Flattened incident data

        Returns:
            list[dict[str, str]]: List of flattened event dicts
        """
        if not incident.properties.alerts:
            flat_incident["kind"] = constants.INCIDENT_EVENT_KIND
            return [flat_incident]

        events = []

        for incident_alert in incident.properties.alerts:
            if (
                incident_alert.is_scheduled_or_nrt()
                and not self.params.use_same_approach
            ):
                if not incident_alert.scheduled_alert:
                    self.logger.info(
                        f"Incident alert {incident_alert.id} is scheduled "
                        f"but has no scheduled alerts data fetched. "
                        f"Incident alert data will be used instead."
                    )
                    events.append(incident_alert.to_event())
                    events.extend(
                        create_regular_alert_events(
                            flat_incident,
                            incident_alert,
                            self.params.create_extra_events_for_all_entities,
                            self.params.product_field_fallback,
                            self.params.fallback_logic_debug,
                        )
                    )
                    continue

                events.extend(
                    create_scheduled_alert_events(
                        flat_incident,
                        incident_alert,
                        self.params.create_extra_events_for_all_entities,
                        self.params.product_field_fallback,
                        self.params.fallback_logic_debug,
                    )
                )

            else:
                # Use the alert itself as the event
                events.append(incident_alert.to_event())

                events.extend(
                    create_regular_alert_events(
                        flat_incident,
                        incident_alert,
                        self.params.create_extra_events_for_all_entities,
                        self.params.product_field_fallback,
                        self.params.fallback_logic_debug,
                    )
                )

        return events

    def _adjust_events_data(self, alert_info: AlertInfo, incident: Incident) -> None:
        """Adjust events data with all additional fields.

        Args:
            alert_info: SOAR alert data model
            incident: Incident data model

        Returns:
            None, update alert_info.events dicts on the spot
        """
        for event in alert_info.events:
            event["properties_title"] = incident.properties.title
            event["properties_incidentNumber"] = incident.properties.incident_number
            event["properties_incidentUrl"] = incident.properties.incident_url
            event["alert_type"] = incident.type
            event["event_type"] = self._get_fallback_value(
                data=event,
                fallback_keys=self.params.event_field_fallback,
                fallback_logic_debug_key="EventFieldFallback",
            )

            event["Siemplify_Start_Time"] = event["SecOps_Start_Time"] = (
                self._get_event_time_value(
                    incident=incident,
                    event=event,
                    fallback_keys=self.params.start_time_fallback,
                    fallback_logic_debug_key="StartTimeFallback",
                )
            )

            event["Siemplify_End_Time"] = event["SecOps_End_Time"] = (
                self._get_event_time_value(
                    incident=incident,
                    event=event,
                    fallback_keys=self.params.end_time_fallback,
                    fallback_logic_debug_key="EndTimeFallback",
                )
            )

    def _get_event_time_value(
        self,
        incident: Incident,
        event: dict,
        fallback_keys: [str],
        fallback_logic_debug_key: str,
    ) -> str:
        """
        Get event time value
        Args:
            incident (Incident): Incident data model
            event (dict): event data
            fallback_keys ([str]): list of keys to use for value extraction
            fallback_logic_debug_key (str): key to set for fallback logic debug

        Returns:
            str: event time value
        """
        value = (
            self._get_fallback_value(
                data=event,
                fallback_keys=fallback_keys,
                fallback_logic_debug_key=fallback_logic_debug_key,
            )
            or incident.properties.created_time_utc
        )

        if value:
            alert_time = value
            if (
                self.params.fallback_logic_debug
                and fallback_logic_debug_key not in event
            ):
                event[fallback_logic_debug_key] = "CreatedTimeUTC"
        else:
            alert_time = utc_now().isoformat()
            if self.params.fallback_logic_debug:
                event[fallback_logic_debug_key] = "Current time"

        return alert_time

    def create_alert_info(self, incident: Incident) -> AlertInfo:
        """Create AlertInfo object out of and Incident data model.

        Args:
            incident: Incident data model

        Returns:
            AlertInfo object
        """
        flat_incident = incident.raw_to_flat_data()
        alert_info = AlertInfo()

        alert_info.display_id = f"{incident.name}_{uuid.uuid4()}"
        alert_info.ticket_id = incident.name
        alert_info.name = get_value_from_template(
            template=self.params.alert_name_template,
            data=flat_incident,
            default_value=incident.properties.title,
        )
        alert_info.rule_generator = get_value_from_template(
            template=self.params.rule_generator_template,
            data=flat_incident,
            default_value=incident.properties.title,
        )
        alert_info.source_grouping_identifier = incident.name
        alert_info.description = incident.properties.description
        alert_info.priority = MicrosoftAzureSentinelParser.calculate_priority(
            incident.properties.severity
        )

        self._set_time_for_alert(
            alert_info=alert_info, incident=incident, flat_incident=flat_incident
        )

        self._set_product_and_vendor_for_alert(
            alert_info=alert_info, incident=incident, flat_incident=flat_incident
        )

        alert_info.extensions = create_extensions(incident.properties)

        alert_info.events = self._build_events_data(
            incident=incident, flat_incident=flat_incident
        )
        alert_info.environment = self.env_common.get_environment(flat_incident)

        self._adjust_events_data(alert_info=alert_info, incident=incident)
        return alert_info

    def _collect_seen_ids(
        self, incident: Incident, existing_ids: dict[str, dict]
    ) -> dict[str, dict]:
        """
        Collect seen ids based on already existing_ids and additional ids from incident

        Args:
            incident (Incident): Incident object which contains additional ids
            existing_ids (dict[str, dict]): Dictionary representing the current seen ids
            The structure of this dictionary is as follows:
                {
                    "<incident_id>": {
                        "ingested_time": <timestamp>,
                        "alerts": {
                            "<alert_1_id>": {
                                "events": [<event_1_hash>, ...],
                                "entities": [<entity_1_id>, ...]
                            }
                        }
                    }
                }

        Returns:
            dict[str, dict]: Dictionary containing collected seen IDs.
            The structure of the returned dictionary is the same as the `existing_ids`
            with additional entries added based on the Incident object.

        Example:
            {
                "<incident_id>": {
                    "ingested_time": <timestamp>,
                    "alerts": {
                        "<alert_1_id>": {
                            "events": [<event_1_hash>, <event_2_hash>],
                            "entities": [<entity_1_id>]
                        },
                        "<alert_2_id>": {
                            "events": [<event_3_hash>],
                            "entities": [<entity_2_id>, <entity_3_id>]
                        }
                    }
                }
            }
        """
        existing_ids = existing_ids or {}

        return {
            "ingested_time": (
                existing_ids.get("ingested_time") or incident.last_modified_time_ts
            ),
            "alerts": {
                **existing_ids.get("alerts", {}),
                **{
                    alert.name: {
                        "events": collect_seen_events_hashes(alert, existing_ids),
                        "entities": collect_seen_entities_ids(alert, existing_ids),
                    }
                    for alert in incident.incident_alerts
                },
            },
        }

    def _already_seen_items(self, incident: Incident) -> bool:
        """
        Check if incident and all related items are already seen
        Args:
            incident (Incident): Incident object

        Returns:
            bool: True if all items are already seen else False
        """
        if incident.name not in self.context.existing_ids.keys():
            return False

        all_seen = True
        new_alerts = []

        for alert in incident.incident_alerts:
            if (
                alert.name
                not in self.context.existing_ids.get(incident.name, {})
                .get("alerts", {})
                .keys()
            ):
                all_seen = False
                new_alerts.append(alert)
                continue

            alert_ids = (
                self.context.existing_ids.get(incident.name)
                .get("alerts")
                .get(alert.name)
            )

            new_events = [
                event
                for event in (
                    (alert.scheduled_alert and alert.scheduled_alert.events) or []
                )
                if dict_to_md5_hash(event) not in alert_ids.get("events", [])
            ]
            new_entities = [
                entity
                for entity in (alert.entities or [])
                if entity.name not in alert_ids.get("entities", [])
            ]

            if new_events or new_entities:
                all_seen = False
                if alert.scheduled_alert:
                    alert.scheduled_alert.events = new_events
                alert.entities = new_entities
                new_alerts.append(alert)

        incident.properties.alerts = new_alerts
        return all_seen

    def _reached_scheduled_alerts_events_limit(self, incident):
        """
        Check if incident reached total number of events limit to ingest
        Args:
            incident (Incident): Incident object

        Returns:
            bool: True if limit is reached else False
        """
        if (
            incident.name not in self.context.existing_ids.keys()
            or self.params.use_same_approach
            or all(
                not incident_alert.is_scheduled_or_nrt()
                for incident_alert in incident.properties.alerts
            )
        ):
            return False

        return (
            self._calculate_existing_scheduled_alerts_events(incident)
            >= self.params.scheduled_alerts_events_limit_to_ingest
        )

    def _calculate_existing_scheduled_alerts_events(self, incident):
        """
        Calculate existing scheduled alerts events amount
        Args:
            incident (Incident): Incident object

        Returns:
            int: Existing scheduled alerts events amount
        """
        total_events = []
        existing_alerts = self.context.existing_ids.get(incident.name, {}).get(
            "alerts", {}
        )

        for items in existing_alerts.values():
            total_events.extend(items.get("events", []))

        return len(total_events)

    def _is_backlog_incident_expired(self, incident_number: str) -> bool:
        """
        Check if backlog incident is expired
        Args:
            incident_number (str): incident number

        Returns:
            bool: True if expired, False otherwise
        """
        backlog_exp_time = (
            self.params.backlog_expiration_timer
            * NUM_OF_SEC_IN_MIN
            * NUM_OF_MILLI_IN_SEC
        )
        incident_backlog_time = self.context.backlog_ids.get(incident_number, 0)
        return self.connector_start_time >= incident_backlog_time + backlog_exp_time


def create_extensions(incident_properties: IncidentProperties) -> dict[str, str]:
    """
    Create extensions for AlertInfo object
    Args:
        incident_properties (IncidentProperties): IncidentProperties object

    Returns:
        dict[str, str]: flat extensions dict
    """
    return dict_to_flat(
        {
            "status": incident_properties.status,
            "labels": [str(label) for label in incident_properties.labels],
            "endTimeUtc": incident_properties.end_time_utc,
            "startTimeUtc": incident_properties.start_time_utc,
            "owner": (
                incident_properties.owner.assigned_to
                if incident_properties.owner
                else None
            ),
            "lastModifiedTimeUtc": incident_properties.last_modified_time_utc,
            "createdTimeUtc": incident_properties.created_time_utc,
            "incidentNumber": incident_properties.incident_number,
            "incidentUri": incident_properties.incident_url,
            "additionalData": incident_properties.additional_data,
        }
    )


def collect_seen_events_hashes(
    alert: IncidentAlert, existing_ids: dict[str, dict]
) -> list[str]:
    """
    Collect seen events hashes based on existing_ids and events from alert

    Args:
        alert (IncidentAlert): IncidentAlert object which contains additional hashes
        existing_ids (dict[str, dict]): Dictionary representing the current seen ids
        The structure of this dictionary is as follows:
            {
                "<incident_id>": {
                    "ingested_time": <timestamp>,
                    "alerts": {
                        "<alert_1_id>": {
                            "events": [<event_1_hash>, ...],
                            "entities": [<entity_1_id>, ...]
                        }
                    }
                }
            }

    Returns:
        [str]: list of seen events hashes
    """
    existing_events_hashes = (
        existing_ids.get("alerts", {}).get(alert.name, {}).get("events", [])
    )
    new_events_hashes = (
        [dict_to_md5_hash(event) for event in alert.scheduled_alert.events]
        if alert.scheduled_alert and alert.scheduled_alert.events
        else []
    )

    return list(set(existing_events_hashes + new_events_hashes))


def collect_seen_entities_ids(
    alert: IncidentAlert, existing_ids: dict[str, dict]
) -> list[str]:
    """
    Collect seen entities ids based on existing_ids and entities from alert

    Args:
        alert (IncidentAlert): IncidentAlert object which contains additional ids
        existing_ids (dict[str, dict]): Dictionary representing the current seen ids
        The structure of this dictionary is as follows:
            {
                "<incident_id>": {
                    "ingested_time": <timestamp>,
                    "alerts": {
                        "<alert_1_id>": {
                            "events": [<event_1_hash>, ...],
                            "entities": [<entity_1_id>, ...]
                        }
                    }
                }
            }

    Returns:
        [str]: list of seen entities ids
    """
    existing_entities_ids = (
        existing_ids.get("alerts", {}).get(alert.name, {}).get("entities", [])
    )
    new_entities_ids = [entity.name for entity in (alert.entities or [])]

    return list(set(existing_entities_ids + new_entities_ids))


async def main() -> None:
    """main"""
    connector = IncidentTrackingConnector()
    await asyncio.ensure_future(connector.start())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
