from __future__ import annotations
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import unquote
from typing import Any

from dateutil.parser import parse as isoparse

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
from utils import extract_and_decode_raw_log, get_timestamps


class ExecuteUDMQuery(Action):

    def __init__(self) -> None:
        super().__init__(consts.EXECUTE_UDM_QUERY_SCRIPT_NAME)

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
        self.params.query = extract_action_param(
            self.soar_action,
            param_name="Query",
            is_mandatory=True,
            print_value=True,
        )
        self.params.include_raw_log = extract_action_param(
            self.soar_action,
            param_name=consts.INCLUDE_RAW_LOG_DATA_PARAM,
            input_type=bool,
            default_value=False,
            print_value=True,
        )
        self.params.time_frame = extract_action_param(
            self.soar_action,
            param_name=consts.TIME_FRAME_PARAM,
            default_value=consts.LAST_HOUR,
            print_value=True,
        )
        self.params.start_time = extract_action_param(
            self.soar_action,
            param_name="Start Time",
        )
        self.params.end_time = extract_action_param(
            self.soar_action,
            param_name="End Time",
        )
        self.params.limit = extract_action_param(
            self.soar_action,
            param_name="Max Results To Return",
            input_type=int,
            default_value=50,
            print_value=True,
        )

    def _validate_params(self) -> None:
        validator: validation.ParameterValidator = validation.ParameterValidator(
            self.soar_action,
        )
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        if (
            self.params.include_raw_log
            and consts.BACKSTORY_API_ROOT_IDENTIFIER in self.params.api_root
        ):
            raise exceptions.GoogleChronicleValidationError(
                "\"Include Raw Log Data\" is only supported for Chronicle API "
                "authentication. Please update the integration configuration or disable"
                " the parameter."
            )

        if self.params.time_frame == consts.CUSTOM:
            if is_empty_string_or_none(self.params.start_time):
                raise exceptions.GoogleChronicleValidationError(
                    f"When '{consts.CUSTOM}' is selected for the "
                    f"'{consts.TIME_FRAME_PARAM}' parameter, you must also provide a "
                    "value for the 'Start Time' parameter."
                )
            self.params.start_time = self._validate_and_format_iso8601(
                self.params.start_time, "Start Time"
            )
            if not is_empty_string_or_none(self.params.end_time):
                self.params.end_time = self._validate_and_format_iso8601(
                    self.params.end_time, "End Time"
                )

        if self.params.limit:
            validator.validate_range(
                param_name="Max Results To Return",
                value=self.params.limit,
                min_limit=consts.MIN_RESULTS_TO_RETURN,
                max_limit=consts.MAX_RESULTS_TO_RETURN,
            )

    def _validate_and_format_iso8601(
        self,
        value: str,
        param_name: str,
    ) -> str:
        try:
            dt_obj = isoparse(value)
            if dt_obj.tzinfo is None:
                dt_obj = dt_obj.replace(tzinfo=timezone.utc)
            return dt_obj.isoformat().replace("+00:00", "Z")
        except (ValueError, TypeError) as error:
            raise exceptions.GoogleChronicleValidationError(
                f"Parameter '{param_name}' must be a valid ISO 8601 "
                f"datetime string. Provided value: '{value}'"
            ) from error

    def _init_api_clients(self) -> GoogleChronicleManager:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _) -> None:
        self.logger.info(f"Starting action {consts.EXECUTE_UDM_QUERY_SCRIPT_NAME}")

        start_time_str: str
        end_time_str: str
        start_time_str, end_time_str = self._get_time_range_strings()

        self.logger.info(
            f"Executing UDM query. Time range: {start_time_str} to "
            f"{end_time_str}. Limit: {self.params.limit}"
        )

        events: list[Any]
        events = self.api_client.get_events_by_udm_query(
            query=self.params.query,
            start_time=start_time_str,
            end_time=end_time_str,
            limit=self.params.limit,
        )
        self.logger.info(f"Found {len(events)} events for the query.")

        event_dicts: list[SingleJson] = self._transform_api_events(events)

        if self.params.include_raw_log and event_dicts:
            self._process_raw_logs(event_dicts)

        self._finalize_events(event_dicts)
        self._set_output(event_dicts)

    def _get_time_range_strings(self) -> tuple[str, str]:
        alert_start_time = self._ms_to_datetime(
            getattr(self.soar_action.current_alert, "start_time", None)
        )
        alert_end_time = self._ms_to_datetime(
            getattr(self.soar_action.current_alert, "end_time", None)
        )

        return get_timestamps(
            range_string=self.params.time_frame,
            start_time_string=self.params.start_time,
            end_time_string=self.params.end_time,
            alert_start_time=alert_start_time,
            alert_end_time=alert_end_time or alert_start_time,
        )

    def _transform_api_events(
        self,
        events: list[Any],
    ) -> list[SingleJson]:
        return [event.to_json() for event in events]

    def _process_raw_logs(
        self,
        event_dicts: list[SingleJson],
    ) -> None:
        self.logger.info("Raw log data inclusion is enabled. Fetching raw logs.")
        event_ids_map: dict[str, list[int]] = self._build_event_id_map(event_dicts)

        if not event_ids_map:
            self.logger.info(
                "No event IDs found in UDM query results to fetch raw logs for."
            )
            return

        self.logger.info(
            f"Found {len(event_ids_map)} unique event IDs to query for raw logs."
        )
        self.logger.info("Fetching raw logs for each event ID individually.")

        for event_id, indices in event_ids_map.items():
            try:
                self._fetch_and_attach_single_raw_log(event_id, indices, event_dicts)
            except exceptions.GoogleChronicleManagerError as e:
                self.logger.error(
                    f"Failed to fetch raw log for event ID {event_id}. Reason: {e}"
                )

    def _build_event_id_map(
        self,
        event_dicts: list[SingleJson],
    ) -> dict[str, list[int]]:
        event_ids_map: dict[str, list[int]] = {}
        for i, event_dict in enumerate(event_dicts):
            event_name: str | None = event_dict.get("name")

            if not event_name:
                continue

            match: re.Match | None = consts.EVENT_ID_PATTERN.search(event_name)
            if not match:
                continue

            event_id: str = unquote(match.group(1))
            if event_id not in event_ids_map:
                event_ids_map[event_id] = []
            event_ids_map[event_id].append(i)

        return event_ids_map

    def _fetch_and_attach_single_raw_log(
        self,
        event_id: str,
        indices: list[int],
        event_dicts: list[SingleJson],
    ) -> None:
        raw_log_objects: list[Any] = self.api_client.get_raw_logs_for_events([event_id])

        decoded_log_content: SingleJson | str | None = extract_and_decode_raw_log(
            raw_log_objects=raw_log_objects,
            event_id=event_id,
            logger=self.logger,
        )

        if not decoded_log_content:
            return

        for index in indices:
            try:
                event_dicts[index].setdefault("udm", {})["rawLogData"] = (
                    decoded_log_content
                )
            except KeyError:
                self.logger.error(f"Malformed event structure at index {index}.")

    def _finalize_events(
        self,
        event_dicts: list[SingleJson],
    ) -> None:
        for event_dict in event_dicts:
            if "name" in event_dict.get("event", {}):
                del event_dict["event"]["name"]

    def _set_output(
        self,
        event_dicts: list[SingleJson],
    ) -> None:
        if event_dicts:
            self.json_results: SingleJson = {"events": event_dicts}
            self.output_message = (
                "Successfully returned results for the query "
                f"“{self.params.query}” in {consts.INTEGRATION_DISPLAY_NAME}."
            )
        else:
            self.output_message = (
                f"No results were found for the query “{self.params.query}” "
                f"in {consts.INTEGRATION_DISPLAY_NAME}"
            )

        self.result_value = True
        self.logger.info(
            f"Action {consts.EXECUTE_UDM_QUERY_SCRIPT_NAME} "
            "finished successfully."
        )

    def _ms_to_datetime(
        self,
        ms: int,
    ) -> datetime | None:
        if ms is None:
            return None
        if isinstance(ms, datetime):
            return ms
        return datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc)


def main() -> None:
    ExecuteUDMQuery().run()


if __name__ == "__main__":
    main()
