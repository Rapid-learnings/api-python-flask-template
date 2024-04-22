import logging
import os
import sys

from celery import Celery
from dotenv import load_dotenv

from app.constants.logger import default_log_level, log_level_mapping

# Load environment variables from .env file
load_dotenv()

# Define configuration variables
HOST: str = os.environ["HOST"]
PORT = int(os.environ["PORT"])

CACHE_PROVIDER: str = os.environ["CACHE_PROVIDER"]

REDIS_HOST: str = os.environ["REDIS_HOST"]
REDIS_PORT: str = os.environ["REDIS_PORT"]
REDIS_PASSWORD: str = os.environ["REDIS_PASSWORD"]

SECRET_KEY: str = os.environ["SECRET_KEY"]
PUBLIC_GCP_BUCKET_NAME: str = os.environ["PUBLIC_GCP_BUCKET_NAME"]
PRIVATE_GCP_BUCKET_NAME: str = os.environ["PRIVATE_GCP_BUCKET_NAME"]

BASE_URL: str = os.environ["BASE_URL"]

# sentry
SENTRY_DSN: str = os.environ["SENTRY_DSN"]

# GET ORIGIN FROM ENV VARIABLES *OR* SET DEFAULT
ORIGIN: str = os.environ["ORIGIN"] if "ORIGIN" in os.environ else "*"

# Determine the log level based on the environment variable
log_level = log_level_mapping.get(os.getenv("LOG_LEVEL"), default_log_level)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)s - %(funcName)s ] - %(message)s",
    level=log_level,
    stream=sys.stdout,  # directing logs to the standard output
)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)s - %(funcName)s ] - %(message)s"
)


def setup_logger(name, level=logging.INFO):
    """To set up as many loggers as you want"""

    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


# Set up the logger
logger = setup_logger(__name__)

celery_app = Celery(
    "celery_app",
    broker=os.getenv("RABBITMQ_BROKER_URL"),
    backend=os.getenv("CELERY_BACKEND_URL"),
)

celery_app.conf.update(
    {
        "task_routes": {
            # "send_welcome_email": {"queue": "send-email"},
            # "send_forget_password_email": {"queue": "send-email"},
        }
    }
)

# Set broker_connection_retry_on_startup to True or False
celery_app.conf.broker_connection_retry_on_startup = True
