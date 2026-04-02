from __future__ import annotations

from TIPCommon import validation
from TIPCommon.base.action import Action, DataTable
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.transformation import construct_csv
from TIPCommon.utils import is_empty_string_or_none

import consts
from exceptions import GoogleChronicleNotFoundError
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2



class GetReferenceLists(Action):

    def __init__(self) -> None:
        super().__init__(consts.GET_REFERENCE_LISTS_SCRIPT_NAME)
        self.error_output_message = "Error executing action " f'"{self.name}".'

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

        self.params.filter_key = extract_action_param(
            self.soar_action, param_name="Filter Key", print_value=True
        )
        self.params.filter_logic = extract_action_param(
            self.soar_action, param_name="Filter Logic", print_value=True
        )
        self.params.filter_value = extract_action_param(
            self.soar_action, param_name="Filter Value", print_value=True
        )
        self.params.expanded_details = extract_action_param(
            self.soar_action,
            param_name="Expanded Details",
            input_type=bool,
            print_value=True,
        )
        self.params.max_reference_list = extract_action_param(
            self.soar_action,
            param_name="Max Reference Lists To Return",
            print_value=True,
        )

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)

        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        self.params.filter_key = validator.validate_ddl(
            param_name="Filter Key",
            value=self.params.filter_key,
            ddl_values=consts.GET_REFERENCE_LIST_FILTER_KEY_DDL_VALUES,
            default_value=consts.GET_REFERENCE_LIST_FILTER_KEY_DEFAULT_VALUE,
        )

        self.params.filter_logic = validator.validate_ddl(
            param_name="Filter Logic",
            value=self.params.filter_logic,
            ddl_values=consts.GET_REFERENCE_LIST_FILTER_LOGIC_DDL_VALUES,
            default_value=consts.GET_REFERENCE_LIST_FILTER_LOGIC_EQUAL,
        )

        self.params.max_reference_list = validator.validate_positive(
            param_name="Max Reference Lists To Return",
            value=self.params.max_reference_list,
        )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _) -> None:
        self.logger.info("Getting the Reference List details")
        filter_key = self.params.filter_key
        filter_logic = self.params.filter_logic
        filter_value = self.params.filter_value
        expanded_details = self.params.expanded_details
        max_reference_list = self.params.max_reference_list

        self.result_value = False

        if filter_key == consts.GET_REFERENCE_LIST_FILTER_KEY_DEFAULT_VALUE:
            self.result_value = False
            raise Exception(
                " you need to select a field from the “Filter Key” parameter."
            )

        list_details = None

        try:
            list_details = self.api_client.get_reference_list(
                filter_value=filter_value,
                filter_key=filter_key,
                filter_logic=filter_logic,
                max_reference_list=max_reference_list,
                expanded_details=expanded_details,
            )

        except GoogleChronicleNotFoundError as e:
            self.logger.error(
                "No reference lists were found for the provided criteria in "
                f"Google Chronicle. Error: {e}"
            )

        self.logger.info(f"Recieived list details {list_details}")

        if list_details:
            list_data = list_details.get_data()
            self.json_results = list_details.to_json()
            self.data_tables.append(
                DataTable(
                    title=consts.GETLIST,
                    data_table=construct_csv(
                        [getdata.to_csv() for getdata in list_data]
                    ),
                )
            )
            self.output_message = (
                "Successfully found reference lists for the provided criteria "
                f"in {consts.INTEGRATION_DISPLAY_NAME}."
            )
            self.result_value = True
            return

        if list_details is None:
            self.output_message = (
                "No reference lists were found for the provided criteria in "
                f'"{consts.INTEGRATION_DISPLAY_NAME}."'
            )
            self.result_value = False
            return

        if filter_value is None:
            self.output_message = (
                "The filter was not applied, because parameter "
                "“Filter Value” has an empty value."
            )
            self.result_value = True
            return


def main() -> None:
    GetReferenceLists().run()


if __name__ == "__main__":
    main()
