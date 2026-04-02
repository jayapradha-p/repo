from __future__ import annotations

from typing import List

from TIPCommon import validation
from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.utils import is_empty_string_or_none

import consts
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from TIPCommon.base.utils import validate_manager


class AddValuesToReferenceList(Action):

    def __init__(self) -> None:
        super().__init__(consts.ADD_VALUES_TO_REFERENCE_LIST_SCRIPT_NAME)
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
            print_value=True,
        )

        self.params.reference_list_name = extract_action_param(
            self.soar_action, param_name="Reference List Name", print_value=True
        )

        self.params.values = extract_action_param(
            self.soar_action, param_name="Values", print_value=True
        )

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        self.params.values = validator.validate_csv(
            param_name="Values", csv_string=self.params.values
        )

    def _init_api_clients(self) -> GoogleChronicleManager:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def remove_empty_input_values(self) -> List:
        return [s for s in self.params.values if s.strip()]

    def _perform_action(self, _) -> None:
        reference_list = self.api_client.get_reference_list_details(
            self.params.reference_list_name
        )
        values = self.remove_empty_input_values()
        update_values = set(values).difference(reference_list.lines)

        if not len(update_values) == consts.ZERO:
            updated_reference_list = self.api_client.add_value_to_reference_list(
                reference_list, update_values
            )
            self.json_results = updated_reference_list.to_json()
        else:
            self.json_results = reference_list.to_json()

        self.output_message = (
            "Successfully added values to the reference list" f" {reference_list.name}"
        )


def main() -> None:
    AddValuesToReferenceList().run()


if __name__ == "__main__":
    main()
