from SiemplifyUtils import unix_now


class Microsoft365DefenderException(Exception):
    """
    General exception for Microsoft 365 Defender
    """

    pass


class TooManyRequestsError(Microsoft365DefenderException):
    def __init__(self, *args, **kwargs):
        self.encountered_at = unix_now()
        self.retry_after = kwargs.pop('retry_after', None)
        super().__init__(*args, **kwargs)


class NotFoundItemException(Microsoft365DefenderException):
    pass


class NotEnoughEntitiesException(Microsoft365DefenderException):
    pass


class APIPermissionError(Microsoft365DefenderException):
    pass


class MissingSeverityFieldError(Microsoft365DefenderException):
    pass


class Microsoft365DefenderNotImplementedException(Microsoft365DefenderException):
    pass


class Microsoft365DefenderServerError(Microsoft365DefenderException):
    """Exception raised when the Microsoft 365 Defender API returns a server error."""
