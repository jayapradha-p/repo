from __future__ import annotations

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param

import constants
import exceptions
from CrowdStrikeManager import CrowdStrikeManager
from datamodels import AlertDetails


class GetAlertDetailsAction(Action):
    """
    Get Alert Details action implementation.
    """

    def __init__(self) -> None:
        super().__init__(constants.GET_ALERT_DETAILS_SCRIPT_NAME)

    def _extract_action_parameters(self) -> None:
        self.params.api_root = extract_configuration_param(
            self.soar_action,
            provider_name=constants.INTEGRATION_NAME,
            param_name="API Root",
            is_mandatory=True,
        )
        self.params.client_id = extract_configuration_param(
            self.soar_action,
            provider_name=constants.INTEGRATION_NAME,
            param_name="Client API ID",
            is_mandatory=True,
        )
        self.params.client_secret = extract_configuration_param(
            self.soar_action,
            provider_name=constants.INTEGRATION_NAME,
            param_name="Client API Secret",
            is_mandatory=True,
        )
        self.params.verify_ssl = extract_configuration_param(
            self.soar_action,
            provider_name=constants.INTEGRATION_NAME,
            param_name="Verify SSL",
            input_type=bool,
            is_mandatory=True,
        )

        self.params.alert_id = extract_action_param(
            self.soar_action,
            param_name="Alert ID",
            is_mandatory=True,
            print_value=True,
        )

    def _init_api_clients(self) -> CrowdStrikeManager:
        return CrowdStrikeManager(
            client_id=self.params.client_id,
            client_secret=self.params.client_secret,
            use_ssl=self.params.verify_ssl,
            api_root=self.params.api_root,
        )

    def _perform_action(self, _) -> None:
        self.logger.info(f"Fetching details for alert ID: {self.params.alert_id}")
        alert_details = self._fetch_alert()
        if not alert_details:
            raise exceptions.AlertNotFoundException(
                f"alert with ID {self.params.alert_id} wasn’t found in Crowdstrike."
                " Please check the spelling."
            )

        self._set_action_result(alert_details[0])

    def _fetch_alert(self) -> list[AlertDetails]:
        try:
            return self.api_client.get_alerts_details(ids=[self.params.alert_id])

        except (
            exceptions.CrowdStrikeNotFoundError,
            exceptions.CrowdStrikeBadRequestError,
        ) as err:
            raise exceptions.AlertNotFoundException(
                f"alert with ID {self.params.alert_id} wasn’t found in Crowdstrike."
                " Please check the spelling."
            ) from err

    def _set_action_result(self, alert_details: AlertDetails) -> None:
        self.json_results = alert_details.to_json()
        self.output_message = (
            "Successfully returned information about the alert with ID "
            f"{self.params.alert_id} in Crowdstrike."
        )


def main() -> None:
    GetAlertDetailsAction().run()


if __name__ == "__main__":
    main()
