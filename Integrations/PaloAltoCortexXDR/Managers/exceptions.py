class XDRNotFoundException(Exception):
    """Raises when required element not found."""


class XDRException(Exception):
    """XDR General exception."""


class XDRAlreadyExistsException(Exception):
    """Raised when element already exists."""


class XDRMissingParametersException(Exception):
    """
    Custom exception to handle validation failures for missing parameters.
    """


class PaloAltoXdrValidationError(Exception):
    """Validation Error for Palo Alto XDR Integration."""


class CortexXDRConnectorException(Exception):
    """Palo alto Cortex connector Exception."""


class TimeoutIsApproachingError(Exception):
    """
    Custom exception to signal that the job's timeout is approaching.
    """
