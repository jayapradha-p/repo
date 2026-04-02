from __future__ import annotations

import requests
from constants import ALREADY_EXISTS_ERR_CODE, ALREADY_EXISTS_ERR_MSG
from exceptions import XDRException, XDRAlreadyExistsException


def validate_response(
    response: requests.Response,
    error_msg: str = "An error occurred",
) -> None:
    """Validate the response from the API call.
    Args:
        response (requests.Response): The response object from the API call.
        error_msg (str): The error message to raise if the response is not valid.
    Raises:
        XDRException: If the response contains an error.
        XDRAlreadyExistsException: If the response indicates that the resource already
        exists.
    """
    try:
        response.raise_for_status()

    except requests.HTTPError as error:
        try:
            response.json()
        except Exception as e:
            raise XDRException(f"{error_msg}: {error} - {response.content}") from e

        if (
            response.json().get("reply", {}).get("err_code") == ALREADY_EXISTS_ERR_CODE
            and response.json().get("reply", {}).get("err_extra")
            == ALREADY_EXISTS_ERR_MSG
        ):
            raise XDRAlreadyExistsException(
                f'{response.json().get("reply", {}).get("err_msg")} - '
                f'{response.json().get("reply", {}).get("err_extra", response.content)}'
            ) from error

        raise XDRException(
            f'{error_msg}: {response.json().get("reply", {}).get("err_msg")} - '
            f'{response.json().get("reply", {}).get("err_extra", response.content)}'
        ) from error
