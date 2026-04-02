from __future__ import annotations

import re

from TIPCommon import validation
from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.types import SingleJson
from TIPCommon.utils import is_empty_string_or_none

import consts
import utils
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2


class GetRuleDetails(Action):

    def __init__(self) -> None:
        super().__init__(consts.GET_RULE_DETAILS_SCRIPT_NAME)

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

    def _validate_params(self) -> None:
        validator = validation.ParameterValidator(self.soar_action)
        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
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
        self.logger.info("Getting the rule details")

        if utils.is_curated_rule_id(self.params.rule_id):
            rule_details: SingleJson = self.api_client.get_curated_rule_details(
                rule_id=self.params.rule_id,
            )
            self.json_results: SingleJson = self._transform_curated_rule_json(
                rule_details.to_json(),
            )
        else:
            rule_details: SingleJson = self.api_client.get_rule_details(
                rule_id=self.params.rule_id,
            )
            self.json_results: SingleJson = rule_details.to_json()

        self.output_message: str = (
            "Successfully fetched information about "
            f"the rule with ID '{self.params.rule_id}' in "
            f"{consts.INTEGRATION_DISPLAY_NAME}."
        )

    def _transform_curated_rule_json(
        self,
        raw_json: SingleJson,
    ) -> SingleJson:
        content_metadata: SingleJson = raw_json.get("contentMetadata", {})
        rule_text: str | None = raw_json.get("ruleText")
        display_name: str | None = content_metadata.get("displayName")

        metadata: SingleJson = _build_metadata_object(
            content_metadata,
            rule_text,
        )
        state: str | None = _extract_result_from_rule_text(rule_text)

        return {
            "name": raw_json.get("name"),
            "displayName": display_name,
            "ruleName": display_name,
            "author": content_metadata.get("author"),
            "metadata": metadata,
            "createTime": content_metadata.get("createTime"),
            "versionCreateTime": content_metadata.get("createTime"),
            "text": rule_text,
            "ruleText": rule_text,
            "compilationState": state,
        }


def _extract_severity_from_rule_text(
    rule_text: str | None,
) -> str | None:
    """
    Extracts the severity from the rule text using regex.
    """
    if not rule_text:
        return None

    match: re.Match | None = re.search(
        consts.SEVERITY_REGEX,
        rule_text,
        re.IGNORECASE,
    )
    return match.group(1) if match else None


def _extract_result_from_rule_text(
    rule_text: str | None,
) -> str | None:
    """
    Extracts the result from the rule text using regex.
    """
    if not rule_text:
        return None

    match: re.Match | None = re.search(
        consts.RESULT_REGEX,
        rule_text,
        re.IGNORECASE,
    )
    return match.group(1) if match else None


def _build_metadata_object(
    content_metadata: SingleJson,
    rule_text: str | None,
) -> SingleJson:
    """
    Builds the metadata object for a curated rule.
    """
    severity: str | None = _extract_severity_from_rule_text(
        rule_text,
    )
    return {
        "author": content_metadata.get("author"),
        "description": content_metadata.get("description"),
        "severity": severity,
    }


def main() -> None:
    GetRuleDetails().run()


if __name__ == "__main__":
    main()
