class CrowdStrikeError(Exception):
    pass


class CrowdStrikeManagerError(CrowdStrikeError):
    pass


class CrowdStrikeStreamError(CrowdStrikeError):
    pass


class CrowdStrikeParameterError(CrowdStrikeError):
    pass


class CrowdStrikeTimeoutError(CrowdStrikeError):
    pass


class CrowdStrikeSessionCreatedError(CrowdStrikeError):
    pass


class CrowdStrikeFalconValidatorException(CrowdStrikeError):
    pass


class NotExistingFilenamesException(CrowdStrikeError):
    pass


class NoSuitableEntitiesException(CrowdStrikeError):
    pass


class FolderNotFoundException(CrowdStrikeError):
    pass


class CrowdStrikeNotFoundError(CrowdStrikeError):
    pass


class CrowdStrikeUnsupportedType(CrowdStrikeError):
    pass


class CrowdStrikeUnauthorisedError(CrowdStrikeError):
    pass


class CrowdStrikeBadRequestError(CrowdStrikeError):
    pass


class CrowdStrikeInvalidUserException(CrowdStrikeError):
    pass


class ODSDetectionLevelError(CrowdStrikeError):
    pass


class ODSInvalidFilePathError(CrowdStrikeError):
    pass


class InvalidCidError(CrowdStrikeError):
    """Raise if invalid customer id provided."""


class AlertNotFoundException(CrowdStrikeError):
    """Raises when Alert not found in Crowdstrike instance."""


class CommentLimitException(CrowdStrikeError):
    """Raises when comment length exceeds more than 1024 characters."""


class InvalidParameterError(Exception):
    """Invalid parameter error."""


class ExpiredJobIdError(Exception):
    """Raises when JobId is expired."""


class CrowdStrikeImproperlyConfiguredError(CrowdStrikeError):
    """Raise if a configuration or definition is incorrect."""
