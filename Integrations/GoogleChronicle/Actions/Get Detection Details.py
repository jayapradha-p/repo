from __future__ import annotations

import re
from datetime import datetime, timedelta
from typing import Any

from TIPCommon import validation
from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.types import SingleJson
from TIPCommon.utils import is_empty_string_or_none

import consts
import exceptions
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from datamodels import Detection
import utils


class GetDetectionDetails(Action):

    def __init__(self) -> None:
        super().__init__(consts.GET_DETECTION_DETAILS_SCRIPT_NAME)

    def _extract_action_parameters(self) -> None:
        self.params.user_service_account = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="User's Service Account",
            remove_whitespaces=False,
        )
        self.params.workload_identity_email = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Workload Identity Email",
        )
        self.params.api_root = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="API Root",
            is_mandatory=True,
            print_value=True,
        )
        self.params.verify_ssl = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Verify SSL",
            is_mandatory=True,
            input_type=bool,
        )
        self.params.rule_id = extract_action_param(
            self.soar_action,
            param_name="Rule ID",
            is_mandatory=True,
            print_value=True,
        )
        self.params.detection_id = extract_action_param(
            self.soar_action,
            param_name="Detection ID",
            is_mandatory=True,
            print_value=True,
        )
        self.params.include_raw_log_data = extract_action_param(
            self.soar_action,
            param_name="Include Raw Log Data",
            input_type=bool,
            is_mandatory=False,
            default_value=False,
            print_value=True,
        )

    def _validate_params(self) -> None:
        validator: validation.ParameterValidator = validation.ParameterValidator(
            self.soar_action,
        )

        if (
            self.params.include_raw_log_data
            and consts.BACKSTORY_API_ROOT_IDENTIFIER in self.params.api_root
        ):
            raise exceptions.GoogleChronicleValidationError(
                "\"Include Raw Log Data\" is only supported for Chronicle API "
                "authentication. Please update the integration configuration or disable"
                " the parameter."
            )

        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account: SingleJson = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _: Any) -> None:
        self.logger.info("Getting the detection details")

        detection_details: Detection
        if utils.is_curated_rule_id(self.params.rule_id):
            detection_details = self._get_curated_detection_details()
        else:
            detection_details = self.api_client.get_detection_details(
                rule_id=self.params.rule_id,
                detection_id=self.params.detection_id,
            )

        json_result: SingleJson = detection_details.to_json()

        if self.params.include_raw_log_data:
            self._enrich_detection_with_raw_logs(json_result)

        self.output_message: str = (
            "Successfully fetched information about "
            f'the detection with ID "{self.params.detection_id}" '
            f"in {consts.INTEGRATION_DISPLAY_NAME}."
        )
        self.json_results: SingleJson = json_result

    def _get_curated_detection_details(self) -> Detection:
        self.logger.info("Curated rule ID identified")
        alert: SingleJson = self.soar_action.current_alert.additional_properties

        self._validate_curated_rule_alert_context(alert)
        detection_time_dt: datetime = self._get_detection_time_from_event()

        return self._find_matching_curated_detection(detection_time_dt)

    def _validate_curated_rule_alert_context(
        self,
        alert: SingleJson,
    ) -> None:
        rule_id: str = alert.get("rule_id", "")
        detection_id: str = alert.get("SiemAlertId", "")

        if rule_id != self.params.rule_id or detection_id != self.params.detection_id:
            raise ValueError(
                "The provided curated rule ID or detection ID don't "
                "belong to the current alert"
            )

    def _get_detection_time_from_event(self) -> datetime:
        event: Any = utils.get_first_event_data(self.soar_action)
        if not is_chronicle_detection(event.device_vendor):
            raise exceptions.GoogleChronicleDetectionBaseError(
                "Failed to find detection! Received curated rule ID, but "
                "The detection is not a Google Chronicle detection."
            )

        detection_time: str | None = getattr(
            event, "additional_properties", {}
        ).get("detectionTime")

        if detection_time is None:
            raise exceptions.GoogleChronicleDetectionBaseError(
                "Could not find detection time for the first event of the "
                "current alert"
            )

        return self._parse_detection_time(detection_time)

    def _find_matching_curated_detection(
        self,
        detection_time_dt: datetime,
    ) -> Detection:
        self.logger.info(
            "Fetching detections by a time range of ±%s minutes "
            "around the current alert's event detections time",
            consts.TIME_RANGE_MINUTES,
        )
        delta: timedelta = timedelta(minutes=consts.TIME_RANGE_MINUTES)
        start_time: str = utils.datetime_to_rfc3339(detection_time_dt - delta)
        end_time: str = utils.datetime_to_rfc3339(detection_time_dt + delta)

        detections: list[Detection]
        detections, _ = self.api_client.list_curated_rule_detections(
            curated_rule_id=self.params.rule_id,
            start_time=start_time,
            end_time=end_time,
        )

        self.logger.info(f"Fetched {len(detections)} detections")
        for detection in detections:
            if detection.id == self.params.detection_id:
                return detection

        raise exceptions.DetectionNotFoundError(
            "Curated detection was not found. Please check the spelling."
        )

    def _parse_detection_time(
        self,
        detection_time: str,
    ) -> datetime:
        self.logger.info("Fetching event detection time")
        try:
            detection_time = consts.NS_DATETIME_PATTERN.sub("Z", detection_time)
            return datetime.strptime(detection_time, consts.DETECTION_TIME_FORMAT)

        except ValueError:
            return datetime.strptime(detection_time, consts.TIME_FORMAT)

    def _enrich_detection_with_raw_logs(
        self,
        json_result: SingleJson,
    ) -> None:
        self.logger.info(
            "Include Raw Log Data parameter is enabled. "
            "Attempting to fetch raw logs."
        )
        event_id_map: SingleJson
        event_id_map = self._build_event_id_map(json_result)

        if not event_id_map:
            self.logger.info(
                "No event IDs found in detection details to fetch raw logs for."
            )
            return

        self.logger.info(
            f"Found {len(event_id_map)} unique event IDs to query for raw logs."
        )

        for event_id, references in event_id_map.items():
            self._process_raw_log_for_event(event_id, references)

    def _build_event_id_map(
        self,
        json_result: SingleJson,
    ) -> SingleJson:
        event_id_map: SingleJson = {}
        collection_elements: list[SingleJson]
        collection_elements = json_result.get("collectionElements", [])

        for element in collection_elements:
            for reference in element.get("references", []):
                event_id: str | None = (
                    reference.get("event", {}).get("metadata", {}).get("id")
                )
                if event_id:
                    event_id_map.setdefault(event_id, []).append(reference)

        return event_id_map

    def _process_raw_log_for_event(
        self,
        event_id: str,
        references: list[SingleJson],
    ) -> None:
        try:
            raw_log_objects: list[Any] = self.api_client.get_raw_logs_for_events(
                [event_id],
            )

            decoded_log_json: SingleJson | None = utils.extract_and_decode_raw_log(
                raw_log_objects=raw_log_objects,
                event_id=event_id,
                logger=self.logger,
            )

            if decoded_log_json:
                self._attach_raw_log_to_references(decoded_log_json, references)
                self.logger.debug(f"Added raw log data for event ID: {event_id}")

        except exceptions.GoogleChronicleManagerError as e:
            self.logger.error(
                f"Failed to fetch raw log for event ID {event_id}. "
                f"Reason: {e}"
            )

    def _attach_raw_log_to_references(
        self,
        decoded_log_json: SingleJson,
        references: list[SingleJson],
    ) -> None:
        for reference in references:
            reference["event"]["rawLogData"] = decoded_log_json


def is_chronicle_detection(device_vendor: str) -> bool:
    """Check if the current alert's device vendor is 'Google Chronicle'

    Args:
        device_vendor: The current alert's device vendor

    Returns:
        bool: True if it is  equal to 'Google Chronicle' else False
    """
    return device_vendor == consts.UNIFIED_CONNECTOR_DEVICE_VENDOR


def main() -> None:
    GetDetectionDetails().run()


if __name__ == "__main__":
    main()
