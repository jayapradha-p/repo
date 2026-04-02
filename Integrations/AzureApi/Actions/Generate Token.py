from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlparse

from TIPCommon.base.utils import CreateSession
from TIPCommon.extraction import extract_action_param

import api_utils
from auth import build_auth_params
from base_action import BaseAction
from constants import (
    GENERATE_TOKEN_SCRIPT_NAME,
    GRANT_TYPE_AUTH_CODE,
    INVALID_AUTH_URL_MESSAGE,
    PARAM_AUTHORIZATION_URL,
    TOKEN_GENERATED_MESSAGE,
    UNABLE_TO_GENERATE_TOKEN_MESSAGE,
)
from exceptions import AzureApiInvalidParameterError

if TYPE_CHECKING:
    from typing import Never


class GenerateTokenAction(BaseAction):
    def __init__(self) -> None:
        super().__init__(GENERATE_TOKEN_SCRIPT_NAME)

    def _init_api_clients(self) -> None:
        pass

    def _extract_action_parameters(self) -> None:
        self.params.authorization_url = extract_action_param(
            self.soar_action,
            param_name=PARAM_AUTHORIZATION_URL,
            is_mandatory=True,
            print_value=True,
        )
        self.params.auth_params = build_auth_params(self.soar_action)

    def _validate_params(self) -> None:
        """Validate parameters."""

    def _extract_code_from_url(self) -> str:
        parsed_url: urlparse = urlparse(self.params.authorization_url)
        query: dict[str, list[str]] = parse_qs(parsed_url.query)
        return query.get("code")[0] if "code" in query else ""

    def _generate_refresh_token(self, code: str) -> str:
        self.logger.info("Generating refresh token using authorization code.")
        payload = {
            "client_id": self.params.auth_params.client_id,
            "client_secret": self.params.auth_params.client_secret,
            "code": code,
            "redirect_uri": self.params.auth_params.redirect_url,
            "grant_type": GRANT_TYPE_AUTH_CODE,
        }
        token_url: str = api_utils.get_full_url(
            api_root=self.params.auth_params.login_api_root,
            endpoint_id="bearer_token_url",
            tenant_id=self.params.auth_params.tenant_id,
        )

        session = CreateSession.create_session()
        response = session.post(
            token_url,
            data=payload,
            verify=self.params.auth_params.verify_ssl,
        )
        api_utils.validate_response(response)
        self.logger.info("Refresh token generated successfully.")

        return response.json().get("refresh_token")

    def _perform_action(self, _: Never) -> None:
        code = self._extract_code_from_url()
        if not code:
            raise AzureApiInvalidParameterError(INVALID_AUTH_URL_MESSAGE)

        refresh_token: str | None = self._generate_refresh_token(code)
        if refresh_token is None:
            raise AzureApiInvalidParameterError(UNABLE_TO_GENERATE_TOKEN_MESSAGE)

        self.output_message = TOKEN_GENERATED_MESSAGE.format(refresh_token)


def main() -> None:
    action = GenerateTokenAction()
    action.run()


if __name__ == "__main__":
    main()
