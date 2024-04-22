from app.exceptions import BaseExceptionClass


class InvalidAuthError(BaseExceptionClass):

    code = 401
    description = "Authentication error."


class InvalidValueError(BaseExceptionClass):
    """
    Exception raised when a provided value for an operation is deemed invalid.
    """

    code = 400
    description = "The provided value is invalid."


class ForbiddenAccessError(BaseExceptionClass):
    code = 403
    description = "Access forbidden."


class InvalidAuthTokenFormatError(BaseExceptionClass):
    """
    Exception raised when the format of the provided authentication token does not meet the expected format.
    """

    code = 400
    description = "Invalid auth token format."


class InvalidTokenError(BaseExceptionClass):
    """Exception raised when a password reset token is invalid or expired."""

    code = 422
    description = "Invalid or expired auth token."


class InvalidEmailOrPasswordError(BaseExceptionClass):
    """
    Exception raised during the authentication process when either the email or password provided is incorrect.
    """

    code = 401
    description = "Invalid email id or password."


class InvalidEmailError(BaseExceptionClass):
    """
    Exception raised when the provided email does not match the required format or validation criteria.
    """

    code = 400
    description = "The provided email is invalid."


class InternalError(BaseExceptionClass):
    """
    Exception raised when there is an internal server error.
    """

    code = 500
    description = "Internal server error."


class GcpUploadError(BaseExceptionClass):
    """
    Exception raised during failures in uploading files to Google Cloud Platform (GCP) storage.

    Attributes:
        code (int): HTTP status code for the error, set to 500.
        description (str): Human-readable error description.

    This exception covers errors related to generating presigned URLs, actual file uploads,
    or any interaction with GCP storage that doesn't perform as expected.
    """

    code = 500
    description = "Failed to upload to GCP."

