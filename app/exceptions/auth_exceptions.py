from app.exceptions import BaseExceptionClass


class PasswordNotComplexError(BaseExceptionClass):
    """
    Exception raised when the provided password does not meet the specified complexity requirements.
    """

    code = 400
    description = "The provided password does not meet complexity requirements."


class EmailAlreadyExistsError(BaseExceptionClass):
    """
    Exception raised when attempting to create or update a user with an email that already exists in the database.
    """

    code = 409
    description = "The provided email already exists."


class UserCreationError(BaseExceptionClass):
    """
    Exception raised when an error occurs during the user creation process.
    """

    code = 400
    description = "Failed to create user."


class UserNotFoundError(BaseExceptionClass):
    """
    Exception raised when a user cannot be found with the provided identifiers.
    """

    code = 404
    description = "User not found."


class NoFieldsToUpdateError(BaseExceptionClass):
    """
    Exception raised when an update operation is requested but no fields to update have been provided.
    """

    code = 400
    description = "No fields have been provided to update."


class UserListFetchError(BaseExceptionClass):
    """
    Exception raised when an error occurs while attempting to fetch the list of users from the database.
    """

    code = 500
    description = "Failed to fetch the list of users."


class InvalidPasswordError(BaseExceptionClass):
    """
    Exception raised when the provided password for a user is incorrect during an authentication or password update process.
    """

    code = 401
    description = "Invalid password."


class UserNameExistError(BaseExceptionClass):
    """
    Exception raised when a user name already present.
    """

    code = 400
    description = "This user name already exist."
