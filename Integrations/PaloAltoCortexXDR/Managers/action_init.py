from __future__ import annotations

from typing import TYPE_CHECKING

from auth import AuthenticatedSession
from utils import get_integration_parameters
from XDRManager import ApiParameters, XDRManager


if TYPE_CHECKING:
    import requests

    from TIPCommon.types import ChronicleSOAR

    from datamodels import IntegrationParameters


def create_api_client(soar_action: ChronicleSOAR) -> XDRManager:
    """Create XDRManager ApiManager client object.

    Args:
        soar_action (ChronicleSOAR): SiemplifyAction object.

    Returns:
        XDRManager: XDRManager object.
    """
    params: IntegrationParameters = get_integration_parameters(soar_action)
    authenticator: AuthenticatedSession[IntegrationParameters] = AuthenticatedSession()
    session: requests.Session = authenticator.authenticate_session(params)
    api_params: ApiParameters = ApiParameters(api_root=params.api_root)

    return XDRManager(
        session=session,
        api_params=api_params,
        logger=soar_action.LOGGER,
    )
