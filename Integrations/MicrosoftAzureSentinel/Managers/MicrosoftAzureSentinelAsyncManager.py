from __future__ import annotations

import asyncio
from asyncio import Task
from copy import copy
from datetime import datetime
import json
from typing import Any
from urllib.parse import urljoin

import httpx

from SiemplifyUtils import convert_string_to_datetime
from TIPCommon.filters import filter_old_alerts
from TIPCommon.types import SingleJson

from constants import (
    DEFAULT_HTTP_REQUEST_TIMEOUT_SECONDS,
    FETCH_INCIDENTS_EVENTS_ERROR_MESSAGE,
    FETCH_TIMEOUT_THRESHOLD,
)
from exceptions import (
    MicrosoftAzureSentinelBadRequestError,
    MicrosoftAzureSentinelConflictError,
    MicrosoftAzureSentinelIncidentNotFoundError,
    MicrosoftAzureSentinelManagerError,
    MicrosoftAzureSentinelNotFoundError,
    MicrosoftAzureSentinelPermissionError,
    MicrosoftAzureSentinelServerError,
    MicrosoftAzureSentinelTimeoutError,
    MicrosoftAzureSentinelUnauthorizedError,
)
import datamodels
from MicrosoftAzureSentinelCommon import MicrosoftAzureSentinelCommon
from MicrosoftAzureSentinelManager import (
    API_ENDPOINTS,
    HEADERS,
    LOGIN_ENDPOINT,
    TIME_FORMAT,
    QueryFilterKeyEnum,
)
from MicrosoftAzureSentinelManagerV2 import MicrosoftAzureSentinelManagerV2
from utils import dict_to_md5_hash


class MicrosoftAzureSentinelAsyncManager(MicrosoftAzureSentinelManagerV2):
    """MicrosoftAzureSentinel Async Manager."""

    def __init__(
        self,
        http_timeout_seconds: int = DEFAULT_HTTP_REQUEST_TIMEOUT_SECONDS,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.async_client = httpx.AsyncClient(
            headers=HEADERS,
            verify=self.verify_ssl,
            timeout=httpx.Timeout(float(http_timeout_seconds)),
            limits=httpx.Limits(max_connections=6, max_keepalive_connections=10),
        )

        self.token = self.fetch_token()
        self.async_client.headers.update({"Authorization": f"Bearer {self.token}"})

    @classmethod
    def get_api_error_message(cls, exception: httpx.HTTPStatusError) -> str:
        """Get API error message.

        Args:
            exception: {Exception} The api error

        Returns:
             error message
        """
        context = exception.response.content.decode()
        try:
            return exception.response.json().get("error", {}).get("message") or context
        except json.decoder.JSONDecodeError:
            return context

    def validate_login_response(
        self, response: httpx.Response, error_msg: str = "An error occurred"
    ) -> None:
        """Login Response Validation.

        Args:
            response: API Response
            error_msg: Error message to change raised one

        Raises:
            MicrosoftAzureSentinelManagerError if response status code is not success
        """
        try:
            response.raise_for_status()

        except httpx.HTTPError as error:
            error_txt = response.json().get("error_description", response.content)

            self.logger.error(
                f"Authentication failed. Error: {error_txt}. "
                f"Request content: {str(response.request.content)}"
            )

            raise MicrosoftAzureSentinelManagerError(
                f"{error_msg}: {error} {error_txt}"
            ) from error

    def validate_response(
        self, response: httpx.Response, error_msg="An error occurred"
    ) -> None:
        """Login Response Validation.

        Args:
            response: API Response
            error_msg: Error message to change raised one

        Raises:
            MicrosoftAzureSentinelBadRequestError   - status code 400
            MicrosoftAzureSentinelUnauthorizedError - status code 401
            MicrosoftAzureSentinelPermissionError   - status code 403
            MicrosoftAzureSentinelNotFoundError     - status code 404
            MicrosoftAzureSentinelConflictError     - status code 409
            MicrosoftAzureSentinelTimeoutError      - status code 429
            MicrosoftAzureSentinelServerError       - status code 500
            MicrosoftAzureSentinelManagerError      - all other status codes
        """
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as error:
            error_message = self.get_api_error_message(error) or error_msg

            error_context = {
                "request_uri": error.request.url,
                "request_body": error.request.content,
                "response_status": response.status_code,
            }

            self.logger.error(
                f"Response validation failed. Error context: {error_context}. "
                f"Error message: {error_message}. "
                f"Response content: {response.content}"
            )

            if response.status_code == 500:
                raise MicrosoftAzureSentinelServerError(error_message) from error

            if response.status_code == 429:
                raise MicrosoftAzureSentinelTimeoutError(error_message) from error

            if response.status_code == 504:
                raise MicrosoftAzureSentinelManagerError(
                    f"Search didn't completed due to timeout. Error: {error_message}"
                ) from error

            if response.status_code == 409:
                raise MicrosoftAzureSentinelConflictError(error_message) from error

            if response.status_code == 404:
                raise MicrosoftAzureSentinelNotFoundError(
                    error_message, error_context=error_context
                ) from error

            if response.status_code == 403:
                raise MicrosoftAzureSentinelPermissionError(error_message) from error

            if response.status_code == 401:
                raise MicrosoftAzureSentinelUnauthorizedError(error_message) from error

            if response.status_code == 400:
                raise MicrosoftAzureSentinelBadRequestError(
                    error_message, error_context=error_context
                ) from error

            raise MicrosoftAzureSentinelManagerError(
                f"{error_msg}: {error} {error_message}"
            ) from error

    def fetch_token(self):
        # type: () -> str
        """
        Fetch authentication token for Devices payloads.
        @return: Access token
        """
        url = urljoin(self.login_url, LOGIN_ENDPOINT.format(self.tenant_id))
        response = httpx.post(
            url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "resource": self.api_root,
                "client_secret": self.client_secret,
            },
            verify=self.verify_ssl,
        )
        self.validate_login_response(
            response, "Failed to connect to the Azure Sentinel Workspace"
        )
        access_token = response.json().get("access_token")

        if access_token:
            return access_token

        error_msg = response.json().get("error_description", response.content)
        raise MicrosoftAzureSentinelManagerError(
            f"Failed fetching token. Error code: {response.status_code}. "
            f"Description: {error_msg}"
        )

    async def run_kql_query(
        self,
        query: str,
        timespan: str | None = None,
        timeout: int | None = None,
        duration: str | None = None,
        limit: int | None = None,
    ) -> datamodels.PrimaryResult:
        """Run KQL query.

        Args:
            query: Query
            timespan: Time span to look for
            timeout: timeout value for the Azure Sentinel hunting rule API call
            duration: Duration (servertimeout)
            limit: How many results should be fetched

        Returns:
            Query Result
        """
        params = {
            "api-version": self._get_endpoint_version("kql_query"),
            "timespan": timespan,
        }

        json_request = {
            "query": f"{query} | limit {limit}" if limit else query,
            "servertimeout": duration,
        }

        json_request = {k: v for k, v in json_request.items() if v}

        if timeout:
            self._add_session_header("Prefer", f"wait={timeout}")

        response = await self.async_client.post(
            self._get_full_url("kql_query"), params=params, json=json_request
        )

        self._remove_session_header("Prefer")

        self.validate_response(response)

        query_result = self.sentinel_parser.build_results(
            raw_json=response.json(),
            method="build_siemplify_primary_result_obj",
            data_key="tables",
        )

        return query_result and query_result[0]

    async def get_incidents_with_new_endpoint(
        self,
        statuses: list[str],
        severities: list[str],
        limit: int,
        existing_ids: set[str],
        next_page_link: str,
        creation_time: datetime = None,
        updated_time: datetime = None,
    ) -> (list[datamodels.Incident], str):
        """
        Get all Incidents including filters.

        Args:
            statuses: Statuses of the incidents to look for
            severities: Severities of the incidents to look for
            limit: How many results should be fetched
            existing_ids: The incident ids that were already processed
            next_page_link: The next page link, to use pagination across
                connector execution
            creation_time: Get incidents with creationTimeUtc greater than
                passed datetime
            updated_time: Get incidents with lastModifiedTimeUtc greater than
                passed datetime

        Returns:
            List of Incident objects AND next page link
        """
        api_parameters = self._build_api_parameters(
            api_version=self._get_endpoint_version("GET_INCIDENTS"),
            creation_time=creation_time,
            updated_time=updated_time,
            time_frame=None,
            statuses=statuses,
            severities=severities,
            asc=True,
            limit=limit,
        )

        request_url, api_parameters = (
            (next_page_link, None)
            if next_page_link
            else (self._get_full_url("GET_INCIDENTS"), api_parameters)
        )

        try:
            response = await self.async_client.get(request_url, params=api_parameters)
        except httpx.TimeoutException:
            self.logger.error(
                "Got timeout error while trying to fetch new incidents. "
                f"API parameters: {api_parameters}"
            )

            raise
        self.validate_response(response)

        json_response = response.json()
        next_page_link = self.sentinel_parser.get_next_page_link(json_response)
        incidents_data = json_response.get("value")

        incidents = filter_old_alerts(
            siemplify=self.siemplify,
            alerts=[
                self.sentinel_parser.build_siemplify_incident_obj(incident_data)
                for incident_data in incidents_data
            ],
            existing_ids=existing_ids,
            id_key="name",
        )

        return incidents, next_page_link

    async def adjust_incidents_alerts_data(
        self,
        incident: datamodels.Incident,
        connector_starting_time: int,
        python_process_timeout: int,
        incidents_alerts_limit_to_ingest: int | None,
        use_same_approach: bool,
        scheduled_alerts_events_limit: int,
        backlog_ids: dict[str, int],
        alerts_for_no_entities: bool,
        wait_for_scheduled_alerts: bool,
        scheduled_alerts_new_events_limit: int = None,
        incident_existing_items: dict[str, dict] = None,
    ) -> datamodels.Incident:
        """
        Get and adjust incident alerts data.

        Args:
            incident: Incidents object
            use_same_approach: Whether to use the same approach with event creation
                for all alert types
            connector_starting_time: Connector start time
            python_process_timeout: The python process timeout
            scheduled_alerts_events_limit: Limit for scheduled alerts events
            incidents_alerts_limit_to_ingest: Limit for alerts per single
                Azure Sentinel incident
            backlog_ids: Backlog ids dict
            alerts_for_no_entities: Create SOAR alerts for incidents without
                entities ?
            wait_for_scheduled_alerts: Wait for scheduled alerts to be fully
                fetched before creating a SOAR alert
            scheduled_alerts_new_events_limit: Limit for scheduled alerts new events
            incident_existing_items: dict of already existing incident items

        Returns:
            None, update incident object on the spot
        """
        try:
            MicrosoftAzureSentinelCommon.raise_if_timeout(
                connector_starting_time, python_process_timeout, FETCH_TIMEOUT_THRESHOLD
            )
            incident.properties.alerts = await self.get_incident_alerts_by_id(
                incident.name, alerts_limit=incidents_alerts_limit_to_ingest
            )

            if not incident.properties.alerts:
                incident.fully_fetched = (
                    incident.properties.additional_data.get("alertsCount") == 0
                )
                return incident

            _scheduled_alerts = []
            _regular_alerts = []

            for alert in copy(incident.properties.alerts):
                if not use_same_approach and alert.is_scheduled_or_nrt():
                    _scheduled_alerts.append(alert)
                    continue

                _regular_alerts.append(alert)

            # Fetch events for Scheduled or NRT if not "Use Same Approach"
            if _scheduled_alerts:
                await self.fetch_scheduled_alerts(
                    _scheduled_alerts,
                    incident,
                    connector_starting_time,
                    python_process_timeout,
                    scheduled_alerts_events_limit,
                    scheduled_alerts_new_events_limit,
                    incident_existing_items,
                )

            # Set entities data for alerts that should be processed in default flow
            await asyncio.gather(
                *[
                    self.set_entities_data(
                        alert,
                        incident,
                        connector_starting_time,
                        python_process_timeout,
                        backlog_ids,
                        alerts_for_no_entities,
                        wait_for_scheduled_alerts,
                    )
                    for alert in _regular_alerts + _scheduled_alerts
                ]
            )

            incident.fully_fetched = all(
                alert.fully_fetched for alert in incident.properties.alerts
            )

        except httpx.TimeoutException:
            self.logger.error(
                "A timeout error occurred when enhancing incident with "
                f"name={incident.name} ({incident.properties.incident_number}). "
                "Connector start time: "
                f"{connector_starting_time}, Current datetime in UTC: "
                f"{datetime.now()}. Python process timeout: "
                f"{python_process_timeout}. Fetch timeout threshold: "
                f"{FETCH_TIMEOUT_THRESHOLD}"
            )

            incident.fully_fetched = False

        return incident

    async def fetch_scheduled_alerts(
        self,
        incident_alerts: list[datamodels.IncidentAlert],
        incident: datamodels.Incident,
        connector_starting_time: int,
        python_process_timeout: int,
        scheduled_alerts_events_limit: int,
        scheduled_alerts_new_events_limit: int = None,
        incident_existing_items: dict = None,
    ) -> None:
        """
        Get and adjust incident alerts data.

        Args:
            incident_alerts: IncidentAlert list
            incident: Incidents object
            connector_starting_time: Connector start time
            python_process_timeout: The python process timeout
            scheduled_alerts_events_limit: Limit for scheduled alerts events
            scheduled_alerts_new_events_limit: Limit for scheduled alerts new events
            incident_existing_items: dict of already existing incident items

        Returns:
            None, update alerts in place
        """
        MicrosoftAzureSentinelCommon.raise_if_timeout(
            connector_starting_time, python_process_timeout, FETCH_TIMEOUT_THRESHOLD
        )
        alert_id_mapping = {
            incident_alert.properties.system_alert_id: incident_alert
            for incident_alert in incident_alerts
        }

        alerts_with_old_api = await self._get_alerts_by_id_parsed(
            *alert_id_mapping.keys(),
            incident_number=incident.properties.incident_number,
        )

        if not alerts_with_old_api:
            self.logger.error(
                f"Failed to fetch incident {incident.name}"
                f" ({incident.properties.incident_number}) scheduled or NRT alerts."
            )
            return

        fetch_alerts_events_tasks = [
            asyncio.create_task(
                self._fetch_alert_events(
                    scheduled_alert,
                    connector_starting_time,
                    python_process_timeout,
                    scheduled_alerts_events_limit,
                    incident,
                )
            )
            for scheduled_alert in alerts_with_old_api
        ]

        try:
            await self.adjust_scheduled_alerts_events(
                incident,
                fetch_alerts_events_tasks,
                scheduled_alerts_new_events_limit,
                alert_id_mapping,
                incident_existing_items,
            )

        finally:
            not_done_tasks = [
                task for task in fetch_alerts_events_tasks if not task.done()
            ]

            for task in not_done_tasks:
                task.cancel()

            if not_done_tasks and scheduled_alerts_new_events_limit == 0:
                for scheduled_alert in alerts_with_old_api:
                    incident_alert = alert_id_mapping[scheduled_alert.system_alert_id]
                    incident_alert.fully_fetched = True

    async def adjust_scheduled_alerts_events(
        self,
        incident: datamodels.Incident,
        fetch_alerts_events_tasks: list[Task],
        scheduled_alerts_new_events_limit: int,
        alert_id_mapping: dict,
        incident_existing_items: dict,
    ):
        """
        Adjust scheduled alerts events
        Args:
            incident (datamodels.Incident): Incident object
            fetch_alerts_events_tasks ([Task]): list of Task objects for alerts events
            scheduled_alerts_new_events_limit: Limit for scheduled alerts new events
            alert_id_mapping (dict): incident alert id mapping to incident alert
            incident_existing_items (dict): dict of already existing incident items
        """
        for completed_task in asyncio.as_completed(fetch_alerts_events_tasks):
            scheduled_alert_object, scheduled_alert_events = await completed_task
            incident_alert = alert_id_mapping[scheduled_alert_object.system_alert_id]
            incident_alert.scheduled_alert = scheduled_alert_object
            incident_alert.fully_fetched = True

            if not scheduled_alert_events:
                self.logger.error(
                    "Failed to fetch events for scheduled or NRT alert "
                    f"{scheduled_alert_object.system_alert_id}. Parent incident "
                    f"{incident.name} ({incident.properties.incident_number}"
                )
                incident_alert.fully_fetched = False

            if scheduled_alerts_new_events_limit is not None:
                scheduled_alert_object.events = []

                for scheduled_alert_event in scheduled_alert_events:
                    if scheduled_alerts_new_events_limit == 0:
                        break

                    scheduled_alert_object.events.append(scheduled_alert_event)

                    if dict_to_md5_hash(
                        scheduled_alert_event
                    ) not in incident_existing_items.get("alerts", {}).get(
                        scheduled_alert_object.system_alert_id, {}
                    ).get("events", []):
                        scheduled_alerts_new_events_limit -= 1

                if scheduled_alerts_new_events_limit == 0:
                    break

            else:
                scheduled_alert_object.events = scheduled_alert_events

    async def _get_alerts_by_id_parsed(self, *ids: str, incident_number: str = None):
        """Get all alerts by provided ids.

        Args:
            *ids: List of alert ids to fetch
            incident_number: Incident Number

        Returns:
            list[ScheduledAlert] list of parsed Scheduled or NRT alerts
        """
        return self.sentinel_parser.build_scheduled_alert_objs(
            await self._get_alerts_by_id(*ids, incident_number=incident_number)
        )

    async def _get_alerts_by_id(
        self, *ids: str, incident_number: str | None = None
    ) -> list[SingleJson]:
        """Get all alerts by provided ids.

        Args:
            ids: IDs of the alerts
            incident_number: Number of the incident

        Returns:
            Alerts
        """
        alert_ids = ", ".join([f'"{x}"' for x in ids])
        query = (
            "SecurityAlert "
            "| summarize arg_max(TimeGenerated, *) by SystemAlertId "
            f"| where SystemAlertId in({alert_ids})"
        )

        try:
            return (await self.run_kql_query(query=query)).to_json()
        except MicrosoftAzureSentinelBadRequestError as err:
            self.logger.error(
                f"Failed to fetch alerts with KQL query. Error: {err}. "
                f"Executed query: {query}. Error context: {err.error_context}."
            )

            if incident_number:
                self.logger.error(
                    f"Incident {incident_number} was skipped because it didn't had "
                    "SystemAlertID value present on the time of ingestion"
                )
                return []
            raise

    async def _fetch_alert_events(
        self,
        scheduled_alert,
        connector_starting_time,
        python_process_timeout,
        scheduled_alerts_events_limit,
        incident,
    ) -> (datamodels.ScheduledAlert, [SingleJson]):
        """Fetch events for scheduled or NRT alert.

        Args:
            scheduled_alert: ScheduledAlert object
            connector_starting_time: Connector start time
            python_process_timeout: The python process timeout
            scheduled_alerts_events_limit: Limit for scheduled alerts events
            incident: Incidents object

        Returns:
            (datamodels.ScheduledAlert, [SingleJson]):
            tuple of ScheduledAlert object and list of its events
        """
        MicrosoftAzureSentinelCommon.raise_if_timeout(
            connector_starting_time, python_process_timeout, FETCH_TIMEOUT_THRESHOLD
        )

        try:
            events = await self._get_alert_events(
                scheduled_alert.raw_data, limit=scheduled_alerts_events_limit
            )
        except MicrosoftAzureSentinelManagerError:
            events = []

            self.logger.error(
                FETCH_INCIDENTS_EVENTS_ERROR_MESSAGE.format(
                    incident_name=incident.name,
                    incident_number=(incident.properties.incident_number),
                    query=(
                        json.loads(
                            scheduled_alert.raw_data.get("ExtendedProperties")
                        ).get("Query")
                    ),
                )
            )

        self.logger.info(
            f"Fetched {len(events)} events for scheduled or NRT "
            f"alert {scheduled_alert.system_alert_id}."
        )

        return scheduled_alert, events

    async def _get_alert_events(
        self, alert: dict[str, Any], limit: int | None = None
    ) -> list[SingleJson]:
        """Get event list for alert.

        Args:
            alert: Alert
            limit {int}: Limit for results

        Returns:
            List of Events
        """
        extended_properties = json.loads(alert.get("ExtendedProperties"))
        start_time = convert_string_to_datetime(
            extended_properties.get("Query Start Time UTC"), "UTC"
        ).strftime(TIME_FORMAT)
        end_time = convert_string_to_datetime(
            extended_properties.get("Query End Time UTC"), "UTC"
        ).strftime(TIME_FORMAT)

        query = extended_properties.get("Query")
        timespan = f"{start_time}/{end_time}"

        return (
            await self.run_kql_query(query=query, timespan=timespan, limit=limit)
        ).to_json()

    async def set_entities_data(
        self,
        alert: datamodels.IncidentAlert,
        incident: datamodels.Incident,
        connector_starting_time: int,
        python_process_timeout: int,
        backlog_ids: dict[str, int],
        alerts_for_no_entities: bool,
        wait_for_scheduled_alerts: bool,
    ) -> None:
        """
        Populate entities for alert from Incident or Alert itself.

        Args:
            alert: IncidentAlert object
            incident: Incidents object
            connector_starting_time: Connector start time
            python_process_timeout: The python process timeout
            backlog_ids: Backlog ids dict
            alerts_for_no_entities: Create SOAR alerts for incidents without entities ?
            wait_for_scheduled_alerts: Wait for scheduled alerts to be fully
                fetched before creating a SOAR alert

        Returns:
            None, update alert in place
        """
        MicrosoftAzureSentinelCommon.raise_if_timeout(
            connector_starting_time, python_process_timeout, FETCH_TIMEOUT_THRESHOLD
        )

        if alert.scheduled_alert and alert.scheduled_alert.events:
            return

        if len(incident.properties.alerts) == 1:
            alert.entities = await self.get_incident_entities(
                alert.properties.system_alert_id,
                incident.properties.incident_number,
                incident.name,
                backlog_ids,
            )
        else:
            alert.entities = await self.get_alert_entities(
                alert.properties.system_alert_id,
                incident.properties.incident_number,
                incident.name,
                backlog_ids,
            )

        entities_count = len(alert.entities) if alert.entities is not None else "N/A"
        self.logger.info(
            f"Fetched and set {entities_count} entities for alert "
            f"{alert.properties.system_alert_id}"
        )
        if self._should_wait_for_scheduled_alert(
            wait_for_scheduled_alerts, alert
        ):
            self.logger.info(
                f"Alert {alert.properties.system_alert_id} is Scheduled Alert / NRT, "
                "but alert data could not be fetched from Azure API."
            )
            alert.fully_fetched = False
            return

        alert.fully_fetched = bool(
            alert.entities
            or (
                not alert.is_scheduled_or_nrt()
                and alerts_for_no_entities
                and alert.entities is not None
            )
        )

    def _should_wait_for_scheduled_alert(
        self, wait_for_scheduled_alerts: bool, alert: datamodels.IncidentAlert
    ) -> bool:
        """
        Check if we should wait for scheduled alert data.

        Args:
            wait_for_scheduled_alerts: Wait for scheduled alerts to be fully
                fetched before creating a SOAR alert
            alert: IncidentAlert object

        Returns:
            True if we should wait for scheduled alert data, False otherwise.
        """
        return (
            wait_for_scheduled_alerts
            and alert.is_scheduled_or_nrt()
            and not alert.scheduled_alert
        )

    async def get_incident_alerts_by_id(
        self, incident_id: str, alerts_limit: int
    ) -> list[datamodels.IncidentAlert]:
        """Get Azure Sentinel alerts related to  specific incident.

        Args:
            incident_id: ID of the incident
            alerts_limit: Maximum amount of alerts to fetch

        Returns:
            List of IncidentAlert objects
        """
        url = self._get_full_url("GET_INCIDENT_ALERTS", incident_name=incident_id)
        api_parameters = self._build_api_parameters(
            api_version=self._get_endpoint_version("GET_INCIDENT_ALERTS"),
            limit=alerts_limit,
        )

        request_started_at = datetime.now()

        try:
            response = await self.async_client.post(url, params=api_parameters)
            self.validate_response(response)
            alerts_data = response.json().get("value", [])
        except httpx.TimeoutException:
            duration_total_seconds = (
                datetime.now() - request_started_at
            ).total_seconds()

            self.logger.error(
                "Timeout error occurred when fetching alerts for incident with id="
                f"{incident_id}. Request started at: {request_started_at}. "
                f"Took {duration_total_seconds} seconds."
            )

            alerts_data = None

        if not alerts_data:
            return []

        return [
            self.sentinel_parser.build_siemplify_incident_alert_obj(alert_data)
            for alert_data in alerts_data
        ][:alerts_limit]

    async def get_alert_entities(
        self,
        alert_id: str,
        incident_number: int,
        incident_id: str,
        backlog_ids: dict[str, int],
    ) -> list[datamodels.AlertEntity] | None:
        """Get Azure Sentinel  entities related to  specific alert from the incident.

        Args:
            alert_id: {str} ID of the alert
            incident_number: {int} The number of the incident
            incident_id: {str} ID of the incident
            backlog_ids: {dict} Backlog ids dict

        Returns:
            List of Entity objects
        """
        url = self._get_full_url("GET_ALERT_ENTITIES", alert_id=alert_id)
        params = {"api-version": self._get_endpoint_version("GET_ALERT_ENTITIES")}
        payload = {
            "expansionId": (API_ENDPOINTS["GET_ALERT_ENTITIES"]["DEFAULT_EXPANSION_ID"])
        }

        try:
            response = await self.async_client.post(url, json=payload, params=params)
            self.validate_response(response)

        except (
            asyncio.CancelledError,
            httpx.TimeoutException,
            asyncio.TimeoutError,
        ) as err:
            self.logger.error(
                f"Got error when getting alert entities. Error type: {type(err)}. "
                f"Error: {err}. Request payload: {payload}. Alert id="
                f"{alert_id}. Incident id={incident_id}."
            )

            raise

        except Exception as e:
            self.logger.error(
                f"Got error when getting alert entities. {e}. "
                f"Request payload: {payload}. Alert id={alert_id}. "
                f"Incident id={incident_id}."
            )
            if isinstance(e, MicrosoftAzureSentinelTimeoutError):
                raise
            if incident_number not in backlog_ids:
                self.logger.error(
                    f"Failed to fetch alert {alert_id} entities. Parent incident "
                    f"{incident_id}"
                )
            return None

        response_data = response.json().get("value", {})
        edges_data = response_data.get("edges", [])
        return [
            self.sentinel_parser.build_siemplify_alert_entity_obj(
                entity_data,
                next(
                    (
                        edge.get("additionalData", {})
                        for edge in edges_data
                        if edge.get("targetEntityId") == entity_data.get("id")
                    ),
                    None,
                ),
            )
            for entity_data in response_data.get("entities", [])
        ]

    async def get_incident_by_number(self, incident_number: str) -> datamodels.Incident:
        """
        Get incident by its number.

        Args:
            incident_number: The number of the incident

        Returns:
            Incident object
        """
        params = {
            "api-version": self._get_endpoint_version("GET_INCIDENTS"),
            QueryFilterKeyEnum.FILTER.value: (
                f"properties/incidentNumber eq {incident_number}"
            ),
        }
        response = await self.async_client.get(
            self._get_full_url("GET_INCIDENTS"), params=params
        )
        self.validate_response(response)
        incident_data = response.json().get("value")

        if not incident_data:
            raise MicrosoftAzureSentinelIncidentNotFoundError(
                incident_number, f"Incident with number {incident_number} was not found"
            )

        return self.sentinel_parser.build_siemplify_incident_obj(incident_data[0])

    async def get_incident_entities(
        self,
        alert_id: str,
        incident_number: int,
        incident_id: str,
        backlog_ids: dict[str, int],
    ) -> list[datamodels.AlertEntity] | None:
        """Get Azure Sentinel entities related to specific incident.

        Args:
            alert_id: {str} Id of the alert
            incident_number: {int} The number of the incident
            incident_id: {str} ID of the incident
            backlog_ids: {dict} Backlog ids dict

        Returns:
            List of Entity objects
        """
        url = self._get_full_url("GET_INCIDENT_ENTITIES", incident_id=incident_id)

        params = {"api-version": self._get_endpoint_version("GET_INCIDENT_ENTITIES")}

        try:
            response = await self.async_client.post(url, params=params)
            self.validate_response(response)

        except (
            asyncio.CancelledError,
            httpx.TimeoutException,
            asyncio.TimeoutError,
        ) as err:
            self.logger.error(
                f"Got error when getting incident entities. Error type: "
                f"{type(err)}. Error: {err}. Alert id="
                f"{alert_id}. Incident id={incident_id}."
            )

        except Exception as e:
            self.logger.error(
                f"Got error when getting incident entities. {e}. "
                f"Alert id={alert_id}. Incident id={incident_id}."
            )

            if isinstance(e, MicrosoftAzureSentinelTimeoutError):
                raise
            if incident_number not in backlog_ids:
                self.logger.error(
                    f"Failed to fetch alert {alert_id} entities. Parent incident "
                    f"{incident_id}"
                )
            return None

        response_data = response.json()
        edges_data = response_data.get("edges", [])

        return [
            self.sentinel_parser.build_siemplify_alert_entity_obj(
                entity_data,
                next(
                    (
                        edge.get("additionalData", {})
                        for edge in edges_data
                        if edge.get("targetEntityId") == entity_data.get("id")
                    ),
                    None,
                ),
            )
            for entity_data in response_data.get("entities", [])
        ]
