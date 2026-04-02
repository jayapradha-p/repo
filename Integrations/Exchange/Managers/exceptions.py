class ExchangeException(Exception):
    """
    General Exchange Exception
    """

    pass


class ExchangeManagerError(ExchangeException):
    """
    General Exception for file operation manager
    """

    pass


class GetUserReplyException(ExchangeException):
    """
    Exception for get user reply
    """

    pass


class NotFoundEmailsException(ExchangeException):
    """
    Exception for not found emails
    """


class UnableToGetValidEmailFromEntity(Exception):
    pass


class NotFoundAttachmentsException(ExchangeException):
    """
    Exception for not found attachments
    """

    pass


class NotSupportedVersionException(ExchangeException):
    """
    Exception for not supported version
    """

    pass


class TimeoutException(ExchangeException):
    """
    Exception for timeout
    """

    pass


class NotFoundException(ExchangeException):
    """
    Exception for not found case
    """

    pass


class IncompleteInfoException(ExchangeException):
    """
    Exception in case incomplete information
    """

    pass


class InvalidParameterException(ExchangeException):
    """
    Exception in case of invalid parameter
    """

    pass


class AccessTypeMismatchException(ExchangeException):
    """
    Exception in case the action logic is against the access type
    set in the integration config - DELEGATE or IMPERSONATE
    """


class SMIMEMailError(ExchangeException):
    """
    Exception in case the email is SMIME,
    adding this to filter out and process only non SMIME mails,
    until we fulfill the FR for decrypting SMIME emails
    """


class MailboxNotFoundError(ExchangeException):
    """
    Exception in case the mailbox is not found.
    """


class ActionFieldError(ExchangeException):
    """
    Exception in case of any action field error - empty, invalid, etc.
    """


class FileError(ExchangeException):
    """
    Exception in case of file related errors
    """


class ExchangeAuthenticationError(ExchangeException):
    """
    Exception in case of invalid credentials
    """


class InvalidBase64ParameterException(ExchangeException):
    """
    Exception in case of invalid base64 parameter
    """
