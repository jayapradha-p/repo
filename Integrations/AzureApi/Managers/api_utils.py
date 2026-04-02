from __future__ import annotations

from urllib.parse import urljoin
import requests

from constants import ENDPOINTS
from exceptions import AzureApiHTTPError


def get_full_url(
    api_root: str,
    endpoint_id: str,
    endpoints: dict[str, str] = None,
    **kwargs,
) -> str:
    """Builds full URL for API endpoint.

    Args:
        api_root (str): The root URL of the API.
        endpoint_id (str): The identifier for the specific endpoint.
        endpoints (dict[str, str], optional): A dictionary mapping endpoint IDs to their
        paths. Defaults to None.
        **kwargs: Additional parameters to format the endpoint path.

    Returns:
        str: The full URL for the API endpoint.
    """
    endpoints = endpoints or ENDPOINTS
    return urljoin(api_root, endpoints[endpoint_id].format(**kwargs))


def validate_response(
    response: requests.Response,
    error_msg: str = "An error occurred",
) -> None:
    """Validate response

    Args:
        response (requests.Response): The response to validate
        error_msg (unicode):  Default message to display on error.
            Defaults to 'An error occurred'.

    Raises:
        MicrosoftGraphMailManagerError: raise MicrosoftGraphMailManagerError
    """
    try:
        response.raise_for_status()

    except requests.HTTPError as error:
        status_code: int = response.status_code
        try:
            error_response = response.json()

            if isinstance(error_response, dict):
                err = error_response.get(
                    "error",
                    error_response.get("message", error_response),
                )
            else:
                err = error_response

            if isinstance(err, dict):
                err_msg = err.get("message", err)
            else:
                err_msg = err

            raise AzureApiHTTPError(
                f"{error_msg}: {err_msg}",
                status_code=status_code,
            ) from error

        except (ValueError, requests.exceptions.JSONDecodeError) as exc:
            raise AzureApiHTTPError(
                f"{error_msg}: {error} {response.content}",
                status_code=status_code,
            ) from exc
