def handle_error(error):
    """Return a custom response for various errors."""
    response = {"message": error.description, "code": error.code}
    return response, error.code
