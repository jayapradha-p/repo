from __future__ import annotations

import datetime

from SiemplifyConnectorsDataModel import AlertInfo
from SiemplifyUtils import convert_string_to_datetime
from TIPCommon.consts import NUM_OF_MILLI_IN_SEC
from TIPCommon.filters import filter_old_alerts
from TIPCommon.smp_io import read_content, read_ids, write_content, write_ids
from TIPCommon.smp_time import convert_string_to_timestamp

from consts import (
    ALERT_TYPES,
    ALERT_TYPE_NAMES,
    MAX_ALLOWED_INGESTION_DELAY_MINUTES,
)
from datamodels import Detection
from utils import (
    UNIX_FORMAT,
    get_filters_by_alert_type,
    get_formatted_date_from_timestamp,
    get_last_success_time,
    pass_filters,
)


IDS_FILE_NAME = "RULE_ids.json"
IDS_DB_KEY = "RULE_ids"
TIMESTAMP_FILE_NAME = "RULE_timestamp.stmp"
TIMESTAMP_DB_KEY = "RULE_timestamp"
NEXT_PAGE_KEY = "RULE_page_token"
TIMESTAMP_KEY = "timestamp"
STORED_IDS_LIMIT = 1000
TIMEOUT_THRESHOLD = 0.8


class RuleAlert:
    def __init__(
        self, siemplify, manager, python_process_timeout, connector_starting_time
    ):
        self.siemplify = siemplify
        self.manager = manager
        self.python_process_timeout = python_process_timeout
        self.connector_starting_time = connector_starting_time
        self.page_token = None
        self.page_start_time = None

    def read_ids(self):
        """
        Read ids from ids file
        :return: {list} list of ids
        """
        existing_ids = read_ids(
            self.siemplify,
            ids_file_name=IDS_FILE_NAME,
            db_key=IDS_DB_KEY,
            default_value_to_return=[],
        )
        self.siemplify.LOGGER.info(
            f"Successfully loaded {len(existing_ids)} existing "
            f"{ALERT_TYPE_NAMES.get(ALERT_TYPES.get('rule'))} ids"
        )
        return existing_ids

    def get_alerts(
        self,
        existing_ids: list[str],
        fetch_limit: int,
        hours_backwards: int,
        fallback_severity: str | None = None,
    ) -> list[Detection]:
        """Get alerts from Chronicle API.

        Args:
            existing_ids (list[str]): List of existing detection ids.
            fetch_limit: {int} limit for results
            hours_backwards: {int} amount of hours from where to fetch alerts
            fallback_severity: {str} fallback severity

        Returns:
            New continuation time, list of Detection objects
        """
        self.page_start_time = get_last_success_time(
            siemplify=self.siemplify,
            offset_with_metric={"hours": hours_backwards},
            time_format=UNIX_FORMAT,
            timestamp_file_name=TIMESTAMP_FILE_NAME,
            timestamp_db_key=TIMESTAMP_DB_KEY,
        )
        self.page_token = read_content(
            siemplify=self.siemplify,
            default_value_to_return="",
            file_name=NEXT_PAGE_KEY,
            db_key=NEXT_PAGE_KEY,
        )

        page_token, page_start_time, alerts = (
            self.manager.stream_detection_alerts_in_connector(
                existing_ids=existing_ids,
                limit=fetch_limit,
                python_process_timeout=self.python_process_timeout,
                connector_starting_time=self.connector_starting_time,
                timeout_threshold=TIMEOUT_THRESHOLD,
                page_token=self.page_token,
                page_start_time=get_formatted_date_from_timestamp(self.page_start_time),
                fallback_severity=fallback_severity,
            )
        )

        for _alert in alerts:
            self.siemplify.LOGGER.info(
                f"Fetched detection {_alert.id} with timestamp {_alert.timestamp}."
            )

        if self.is_alert_ingestion_delayed(alerts):
            self.siemplify.LOGGER.warn(
                "WARNING: Slow Alert Ingestion! "
                "Security alerts are taking longer than expected to be processed "
                f"(over {MAX_ALLOWED_INGESTION_DELAY_MINUTES} minutes). "
                "This may delay incident response. Please check your connector "
                "configuration to improve performance, or contact support for help."
            )


        self.siemplify.LOGGER.info(
            f"Received nextPageToken: {page_token}, "
            f"nextPageStartTime: {page_start_time}."
        )
        self.page_token = page_token or ""
        self.page_start_time = (
            int(convert_string_to_timestamp(page_start_time)) * NUM_OF_MILLI_IN_SEC
            if page_start_time is not None
            else None
        )

        return sorted(alerts, key=lambda alert: int(getattr(alert, TIMESTAMP_KEY)))

    def filter_alerts(
        self, alerts: list[Detection], existing_ids: list[str]
    ) -> list[Detection]:
        """Filter detections based on existing ids.

        Args:
            alerts (list[Detection]): List of fetched detections.
            existing_ids (list[str]): List of existing detection ids.

        Returns:
            list[Detection]: List of filtered detections.
        """
        filtered_alerts = filter_old_alerts(self.siemplify, alerts, existing_ids, "id")
        self.siemplify.LOGGER.info(
            f"Filtered {len(filtered_alerts)} "
            f"{ALERT_TYPE_NAMES.get(ALERT_TYPES.get('rule'))} alerts."
        )
        return filtered_alerts

    def pass_filters(self, alert):
        filters = get_filters_by_alert_type(
            self.siemplify.LOGGER, self.siemplify.whitelist, ALERT_TYPES.get("rule")
        )
        return pass_filters(self.siemplify.LOGGER, alert, filters)

    def write_ids(self, existing_ids):
        """
        Write ids to ids file
        :param existing_ids: {list} list of existing ids
        :return: {void}
        """
        write_ids(
            self.siemplify,
            existing_ids,
            ids_file_name=IDS_FILE_NAME,
            db_key=IDS_DB_KEY,
            default_value_to_set=[],
            stored_ids_limit=STORED_IDS_LIMIT,
        )

    def save_timestamp(self, alerts: list, incrementation_value: int = 0) -> None:
        """Save last timestamp for given alerts.

        Args:
            alerts: {list} list of Detection objects
            incrementation_value: {int} incrementation value

        Returns:
            None
        """
        write_content(
            self.siemplify,
            self.page_token,
            file_name=NEXT_PAGE_KEY,
            db_key=NEXT_PAGE_KEY,
        )
        write_content(
            self.siemplify,
            self.page_start_time or 0,
            file_name=TIMESTAMP_FILE_NAME,
            db_key=TIMESTAMP_DB_KEY,
        )

    @staticmethod
    def is_alert_ingestion_delayed(alerts: list[Detection]) -> bool:
        """checks for possible ingestion delays between SIEM and SOAR

        Args:
            detections: list of Detection objects

        Returns:
            bool:
                `True` if the detections creation is much earlier then current time,
                `False` otherwise
        """
        if not alerts:
            return False

        latest_detection_dt = max(
            convert_string_to_datetime(detection.created_time)
            for detection in alerts
        ).astimezone(datetime.timezone.utc)
        allowed_delay = datetime.timedelta(
            minutes=MAX_ALLOWED_INGESTION_DELAY_MINUTES
        )
        now = datetime.datetime.now(datetime.timezone.utc)
        return now - latest_detection_dt > allowed_delay

    @staticmethod
    def get_alert_info(
        alert, environment_common, device_product_field
    ):
        """
        Get alert info
        :param alert: {Detection} Detection object
        :param environment_common: {EnvironmentHandle} environment common object for fetching the environment
        :param device_product_field: {str} key to use for device product extraction
        :return: {AlertInfo} AlertInfo object
        """
        return alert.as_unified_alert_info(
            AlertInfo(), environment_common, device_product_field
        )
