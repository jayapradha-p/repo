class AzureApiError(Exception):
    """General exception for Azure API."""


class AzureApiInvalidParameterError(AzureApiError):
    """Invalid Parameter error."""


class AzureApiHTTPError(AzureApiError):
    """Exception in case of HTTP error."""

    def __init__(self, message, *args, status_code=None) -> None:
        super().__init__(message, *args)
        self.status_code = status_code


class InvalidRequestParametersError(AzureApiError):
    """Invalid HTTP Requests Parameters Error."""


class InvalidCredsError(AzureApiError):
    """Invalid Credentials Error."""


class AzureApiInvalidJsonError(AzureApiError):
    """Invalid JSON exception."""


class AzureApiFileError(AzureApiError):
    """File exception."""


class AzureApiJobNotSupportedError(AzureApiError):
    """Job not supported exception."""