class MicrosoftAzureSentinelError(Exception):
    pass


class TimeoutIsApproachingError(MicrosoftAzureSentinelError):
    pass


class MicrosoftAzureSentinelManagerError(MicrosoftAzureSentinelError):
    def __init__(self, *args, **kwargs):
        self.error_context = kwargs.get("error_context", {})
        super().__init__(*args)


class MicrosoftAzureSentinelPermissionError(MicrosoftAzureSentinelManagerError):
    pass


class MicrosoftAzureSentinelUnauthorizedError(MicrosoftAzureSentinelManagerError):
    pass


class MicrosoftAzureSentinelBadRequestError(MicrosoftAzureSentinelManagerError):
    pass


class MicrosoftAzureSentinelNotFoundError(MicrosoftAzureSentinelManagerError):
    pass


class MicrosoftAzureSentinelValidationError(MicrosoftAzureSentinelError):
    pass


class MicrosoftAzureSentinelTimeoutError(MicrosoftAzureSentinelError):
    pass


class MicrosoftAzureSentinelConflictError(MicrosoftAzureSentinelError):
    pass


class MicrosoftAzureSentinelServerError(MicrosoftAzureSentinelError):
    """Microsoft Azure Sentinel Server Error."""


class InvalidParameterError(MicrosoftAzureSentinelError):
    """
    Exception in case of invalid parameter
    """

    pass


class MicrosoftAzureSentinelIncidentNotFoundError(MicrosoftAzureSentinelManagerError):
    """Exception in case of not found incident"""
