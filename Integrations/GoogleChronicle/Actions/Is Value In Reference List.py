from __future__ import annotations

from SiemplifyUtils import convert_dict_to_json_result_dict
from TIPCommon import validation
from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.transformation import convert_list_to_comma_string
from TIPCommon.utils import is_empty_string_or_none

import consts
from exceptions import GoogleChronicleNotFoundError
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2


class IsValueInReferenceList(Action):

    def __init__(self) -> None:
        super().__init__(consts.IS_VALUE_IN_REFERENCE_IN_LIST_SCRIPT_NAME)
        self.output_message = (
            "Successfully searched provided values in the "
            f"reference lists in {consts.INTEGRATION_DISPLAY_NAME}."
        )
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

        self.params.reference_list_names = extract_action_param(
            self.soar_action,
            param_name="Reference List Names",
            is_mandatory=True,
            print_value=True,
        )

        self.params.values = extract_action_param(
            self.soar_action, param_name="Values", is_mandatory=True, print_value=True
        )

        self.params.case_insensitive_search = extract_action_param(
            self.soar_action,
            param_name="Case Insensitive Search",
            is_mandatory=False,
            print_value=True,
            input_type=bool,
            default_value=True,
        )

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)

        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        self.params.reference_list_names = validator.validate_csv(
            param_name="Reference List", csv_string=self.params.reference_list_names
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

    def _perform_action(self, _) -> None:
        self.logger.info("Getting the reference list")
        reference_list_found = []
        reference_list_not_found = []

        for reference_list_name in self.params.reference_list_names:
            try:
                reference_list = self.api_client.get_reference_list_details(
                    reference_list_name
                )
                reference_list_found.append(reference_list)

            except GoogleChronicleNotFoundError:
                reference_list_not_found.append(reference_list_name)

        if reference_list_not_found:
            reference_list_not_found_csv = convert_list_to_comma_string(
                reference_list_not_found
            )
            raise Exception(
                "The following reference lists were not found in "
                f"{consts.INTEGRATION_NAME}: "
                f"{reference_list_not_found_csv}. Please use action "
                '"Get Reference Lists" to see, '
                "what reference lists are available."
            )

        if self.params.case_insensitive_search:
            for reference_list in reference_list_found:
                reference_list.lines = [value.lower() for value in reference_list.lines]

        result = {}
        for value in self.params.values:
            found_list = []
            not_found_list = []
            overall_status = "not found"
            result_json = {}
            for reference_list in reference_list_found:
                if (
                    self.params.case_insensitive_search
                    and value.lower() in [s.strip() for s in reference_list.lines]
                ):
                    found_list.append(reference_list.name)
                elif value in [s.strip() for s in reference_list.lines]:
                    found_list.append(reference_list.name)
                else:
                    not_found_list.append(reference_list.name)

            if found_list:
                overall_status = "found"
            result_json.update(
                {
                    "found_in": convert_list_to_comma_string(found_list),
                    "not_found_in": convert_list_to_comma_string(not_found_list),
                    "overall_status": overall_status,
                }
            )
            result.update({value: result_json})
        self.json_results = convert_dict_to_json_result_dict(result)


def main() -> None:
    IsValueInReferenceList().run()


if __name__ == "__main__":
    main()
