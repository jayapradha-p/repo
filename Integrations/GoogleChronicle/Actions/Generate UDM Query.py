from __future__ import annotations

from typing import TYPE_CHECKING

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon import validation
from TIPCommon.utils import is_empty_string_or_none

import consts
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory

if TYPE_CHECKING:
    from TIPCommon.types import SingleJson


class GenerateUDMQuery(Action):

    def __init__(self) -> None:
        super().__init__(consts.GENERATE_UDM_QUERY_SCRIPT_NAME)
        self.output_message: str = (
            "Successfully generated a UDM query in Google SecOps."
        )

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

        self.params.prompt = extract_action_param(
            self.soar_action,
            param_name="Prompt",
            print_value=True,
            is_mandatory=True,
        )

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )
        validate_api_root_for_backstory(self.params.api_root)

    def _init_api_clients(self) -> GoogleChronicleManager:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _=None) -> None:
        results: SingleJson = self.api_client.generate_udm_query(self.params.prompt)
        self.json_results: SingleJson = results


def main() -> None:
    action = GenerateUDMQuery()
    action.run()


if __name__ == "__main__":
    main()
