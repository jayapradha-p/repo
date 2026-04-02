class GoogleChronicleManagerError(Exception):
    """
    General Exception for Google Chronicle manager
    """


class GoogleChronicleAPILimitError(Exception):
    """
    API Limit Exception for Google Chronicle manager
    """


class GoogleChronicleValidationError(Exception):
    """
    Validation Exception for Google Chronicle manager
    """


class GoogleChronicleParameterValidationError(Exception):
    """
    Parameter Validation Exception for Google Chronicle manager
    """


class GoogleChronicleAuthenticationError(Exception):
    """
    Authentication Exception for Google Chronicle manager
    """


class InvalidTimeException(Exception):
    """
    Exception for invalid time
    """


class GoogleChronicleBadRequestError(Exception):
    """
    Exception for Bad Request
    """


class GoogleChroniclePlatformUnsupportedError(Exception):
    """
    The integration code is not compatible with current Platform version.
    """


class GoogleChronicleNotFoundError(GoogleChronicleManagerError):
    """When requested entity is not found in Google Chronicle"""


class GoogleChronicleDetectionBaseError(Exception):
    """ "Base exception for detection related errors"""


class DetectionNotFoundError(GoogleChronicleDetectionBaseError):
    """Detection cannot be found"""


class DetectionParsingError(GoogleChronicleDetectionBaseError):
    """Detection or Detection parts could not be parsed"""


class GoogleChroniclePermissionError(Exception):
    """Permission error for Google Chronicle manager"""


class InvalidParameterError(Exception):
    """Indicates that parameter value is invalid."""
