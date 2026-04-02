from __future__ import annotations

from SiemplifyUtils import convert_unixtime_to_datetime

from TIPCommon import validation
from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.utils import is_empty_string_or_none

import consts
import exceptions
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2

import utils


class ExecuteRetrohunt(Action):

    def __init__(self) -> None:
        super().__init__(consts.EXECUTE_RETROHUNT_SCRIPT_NAME)
        self.error_output_message = f'Error executing action "{self.name}".'

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
            self.soar_action, param_name="Rule ID", is_mandatory=True, print_value=True
        )
        self.params.time_frame = extract_action_param(
            self.soar_action, param_name="Time Frame", print_value=True
        )
        self.params.start_time = extract_action_param(
            self.soar_action, param_name="Start Time", print_value=True
        )
        self.params.end_time = extract_action_param(
            self.soar_action, param_name="End Time", print_value=True
        )

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        self.params.time_frame = validator.validate_ddl(
            param_name="Time Frame",
            value=self.params.time_frame,
            ddl_values=consts.EXECUTE_RETROHUNT_TIME_FRAME_DDL_VALUES,
            default_value=consts.EXECUTE_RETROHUNT_TIME_FRAME_DEFAULT_VALUE,
        )

    def _init_api_clients(self) -> GoogleChronicleManager:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email
        )

    def _perform_action(self, _) -> None:
        self.logger.info("Executing a rule retrohunt")

        alert_start_time = convert_unixtime_to_datetime(
            int(self._soar_action._current_alert.additional_properties.get("StartTime"))
        )
        alert_end_time = convert_unixtime_to_datetime(
            int(self._soar_action._current_alert.additional_properties.get("EndTime"))
        )
        try:
            start_time, end_time = utils.get_timestamps(
                self.params.time_frame,
                self.params.start_time,
                self.params.end_time,
                alert_start_time,
                alert_end_time,
            )
            execute_retrohunt = self.api_client.execute_retrohunt(
                rule_id=self.params.rule_id, start_time=start_time, end_time=end_time
            )

            self.json_results = execute_retrohunt.to_json()
            self.output_message = (
                "Successfully executed a retrohunt for the provided rule in "
                f"{consts.INTEGRATION_DISPLAY_NAME}."
            )
        except exceptions.InvalidTimeException as err:
            self.result_value = False
            raise err


def main() -> None:
    ExecuteRetrohunt().run()


if __name__ == "__main__":
    main()
