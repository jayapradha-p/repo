from __future__ import annotations

import json
from typing import Any

from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.validation import ParameterValidator

import consts
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory


class AskGemini(Action):
    def __init__(self) -> None:
        super().__init__(consts.ASK_GEMINI_SCRIPT_NAME)
        self.error_output_message = (
            f'Error executing action "{consts.ASK_GEMINI_SCRIPT_NAME}".'
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
        )
        self.params.automatic_opt_in = extract_action_param(
            self.soar_action,
            param_name="Automatic Opt-in",
            print_value=True,
            input_type=bool,
        )
        self.params.prompt = extract_action_param(
            self.soar_action,
            param_name="Prompt",
            print_value=True,
            is_mandatory=True,
        )

    def _validate_params(self) -> None:
        validate_api_root_for_backstory(self.params.api_root)
        validator = ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
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

    def _perform_action(self, _: Any = None) -> None:
        self.api_client.opt_into_gemini(self.params.automatic_opt_in)
        conversation = self.api_client.create_conversation()
        conversation_id = None
        try:
            conversation_id = conversation.raw_data.get("name").split("/")[-1]
            response = self.api_client.execute_prompt(
                conversation_id, self.params.prompt
            )
            self.result_value = True
            self.output_message = "Successfully executed a prompt in Google SecOps."
            self.soar_action.result.add_result_json(json.dumps(response.to_json()))
        finally:
            if conversation_id:
                self.api_client.delete_conversation(conversation_id)


def main() -> None:
    AskGemini().run()


if __name__ == "__main__":
    main()
