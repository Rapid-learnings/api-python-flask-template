import logging

# or doesn't have a valid log level value
default_log_level = logging.ERROR

# Map log level names to their corresponding logging constants
log_level_mapping = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}
