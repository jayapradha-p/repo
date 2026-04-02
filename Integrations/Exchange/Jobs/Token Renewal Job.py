from __future__ import annotations

from collections.abc import MutableMapping

from TIPCommon.base.job import RefreshTokenRenewalJob, validate_param_csv_to_multi_value

from ExchangeManager import ExchangeManager
from constants import INTEGRATION_NAME, TOKEN_RENEWAL_SCRIPT_NAME
from exceptions import ExchangeManagerError


class RefreshTokenJob(RefreshTokenRenewalJob):
    """
    Refresh Token Renewal Job to update refresh token periodically.
    """

    def __init__(self, script_name: str, integration_identifier: str) -> None:
        super().__init__(script_name, integration_identifier)
        self.error_msg = f"{script_name} failed to run because "

    def _get_integration_envs(self) -> str:
        return self.params.integration_environments

    def _get_connector_names(self) -> str:
        return self.params.connector_names

    def _validate_params(self) -> None:
        """Validate the parameters values.

        Raises:
           ExchangeManagerError: In case of integration environments and
               connector names are not provided.
        """
        self.params.integration_environments = validate_param_csv_to_multi_value(
            param_name="Integration Environments",
            param_csv_value=self.params.integration_environments,
        )
        self.params.connector_names = validate_param_csv_to_multi_value(
            param_name="Connector Names",
            param_csv_value=self.params.connector_names,
        )
        if not self.params.integration_environments and not self.params.connector_names:
            raise ExchangeManagerError(
                f"{self.error_msg} both Integration Environments "
                "and Connector Names parameters are not provided."
            )

    def _build_manager_for_instance(
        self,
        instance_settings: MutableMapping[str, str],
    ) -> ExchangeManager:
        """Build Manager object to get the refresh token for integration/connector
        instances.

        Args:
            instance_settings (MutableMapping[str, str]): instance configuration
            settings.

        Returns:
            ExchangeManager: exception while creating ExchangeManager object.
        """
        try:
            return ExchangeManager(
                exchange_server_ip=instance_settings.get(
                    "ServerAddress", instance_settings.get("Mail Server Address")
                ),
                domain=None,
                user_mail_address=instance_settings.get("Mail Address"),
                siemplify_logger=self.logger,
                client_id=instance_settings.get("Client ID"),
                client_secret=instance_settings.get("Client Secret"),
                tenant_id=instance_settings.get("Tenant (Directory) ID"),
                auth_token=instance_settings.get("Refresh Token"),
                verify_ssl=instance_settings.get("Verify SSL").lower() == "true",
            )
        except Exception as e: # pylint: disable=broad-except
            self.logger.error(
                "This instance isn't set up to be used with Oauth, aborting ..."
            )
            self.logger.exception(e)
            return None

    def _refresh_integration_token(self, instance_identifier: str) -> None:
        """Renew refresh token and set it in integration's configuration.

        Args:
            instance_identifier (str): integration instance identifier.
                e.g.: "ce0027a2-2b53-4cce-ad08-430df6d002f3"
        """
        refresh_token = self.api_client.credentials.access_token["refresh_token"]
        self.soar_job.set_configuration_property(
            integration_instance_identifier=instance_identifier,
            property_name="Refresh Token",
            property_value=refresh_token,
        )

    def _refresh_connector_token(self, instance_identifier: str) -> None:
        """Renew refresh token and set it in connector's configuration.
        Args:
            instance_identifier (str): connector instance identifier.
                e.g.: "Test_OauthConnector_75098aae-de81-44cc-a807-4843d5ae7ea5"
        """
        refresh_token = self.api_client.credentials.access_token["refresh_token"]
        self.soar_job.set_connector_parameter(
            connector_instance_identifier=instance_identifier,
            parameter_name="Refresh Token",
            parameter_value=refresh_token,
        )


def main() -> None:
    RefreshTokenJob(TOKEN_RENEWAL_SCRIPT_NAME, INTEGRATION_NAME).start()


if __name__ == "__main__":
    main()
