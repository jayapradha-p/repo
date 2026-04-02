from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from TIPCommon.extraction import extract_action_param
from TIPCommon.transformation import string_to_multi_value

from api_utils import get_full_url
from auth import build_auth_params
from base_action import BaseAction
from constants import (
    AUTH_URL_GENERATED_MESSAGE,
    BROWSE_AUTH_LINK_MESSAGE,
    GET_AUTHORIZATION_SCRIPT_NAME,
    INTEGRATION_IDENTIFIER,
    PARAM_OAUTH_SCOPES,
    RESPONSE_MODE_QUERY,
    RESPONSE_TYPE_CODE,
)

if TYPE_CHECKING:
    from typing import Never


class GetAuthorizationAction(BaseAction):
    def __init__(self) -> None:
        super().__init__(GET_AUTHORIZATION_SCRIPT_NAME)
        self.identifier = INTEGRATION_IDENTIFIER
        self.result_value = True

    def _extract_action_parameters(self) -> None:
        """Extract action parameters."""
        self.params.oauth_scopes = string_to_multi_value(
            extract_action_param(
                self.soar_action,
                param_name=PARAM_OAUTH_SCOPES,
                is_mandatory=True,
                print_value=True,
            ),
            only_unique=True,
        )
        self.params.auth_params = build_auth_params(self.soar_action)

    def _validate_params(self) -> None:
        """Validate parameters."""

    def _init_api_clients(self):
        """Initialize API clients."""

    def _get_authorization_url(self) -> str:
        root_url: str = get_full_url(
            api_root=self.params.auth_params.login_api_root,
            endpoint_id="authorize_url",
            tenant_id=self.params.auth_params.tenant_id,
        )
        scope: str = " ".join(self.params.oauth_scopes)
        params: dict[str, str] = {
            "client_id": self.params.auth_params.client_id,
            "redirect_uri": self.params.auth_params.redirect_url,
            "response_type": RESPONSE_TYPE_CODE,
            "response_mode": RESPONSE_MODE_QUERY,
            "scope": f"{scope}",
        }
        return f"{root_url}?{urlencode(params)}"

    def _perform_action(self, _: Never) -> None:
        authorization_url: str = self._get_authorization_url()
        self.logger.info(f"Generated authorization URL: {authorization_url}")
        self.soar_action.result.add_link(BROWSE_AUTH_LINK_MESSAGE, authorization_url)
        self.output_message = AUTH_URL_GENERATED_MESSAGE


def main() -> None:
    action = GetAuthorizationAction()
    action.run()


if __name__ == "__main__":
    main()
