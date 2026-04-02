from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

from TIPCommon.base.action import Action

from api_client import ApiParameters, AzureApiClient
from auth import (
    AuthenticatedSession,
    build_auth_params,
    SessionAuthenticationParameters,
)
from data_models import IntegrationPlaceholders

if TYPE_CHECKING:
    pass


class BaseAction(Action, ABC):
    def _init_api_clients(self) -> AzureApiClient:
        auth_params = build_auth_params(self.soar_action)
        authenticator: AuthenticatedSession = AuthenticatedSession()
        auth_params_for_session = SessionAuthenticationParameters(
            login_api_root=auth_params.login_api_root,
            api_root=auth_params.api_root,
            tenant_id=auth_params.tenant_id,
            client_id=auth_params.client_id,
            client_secret=auth_params.client_secret,
            verify_ssl=auth_params.verify_ssl,
            refresh_token=auth_params.refresh_token,
            scopes=auth_params.scopes,
            redirect_url=auth_params.redirect_url,
        )
        authenticator.authenticate_session(auth_params_for_session)

        api_params: ApiParameters = ApiParameters(
            api_root=auth_params.api_root,
            tenant_id=auth_params.tenant_id,
        )

        return AzureApiClient(
            authenticated_session=authenticator.session,
            configuration=api_params,
            placeholders=IntegrationPlaceholders(),
            logger=self.logger,
        )

    @property
    def result_value(self) -> bool:
        return self._result_value

    @result_value.setter
    def result_value(self, value: bool) -> None:
        self._result_value = value
