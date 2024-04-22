import os

from app.logs.sentry import sentry_client
from dotenv import load_dotenv
from flask_pymongo import PyMongo

# Load environment variables from a .env file
load_dotenv()

MONGO_URI = os.environ["MONGO_URI"]


class MongoDBConnection:
    # Class variable to hold the single instance of MongoDBConnection
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Check if an instance already exists
        if not cls._instance:
            # If not, create a new instance
            cls._instance = super(MongoDBConnection, cls).__new__(cls, *args, **kwargs)
            # Initialize the PyMongo instance
            cls._instance._mongo = PyMongo()

        # Return the existing or new instance
        return cls._instance

    @property
    def get_connection(self):
        # Return the PyMongo instance
        return self._instance._mongo

    def init_app(self, app):
        try:
            # Initialize the PyMongo instance with the Flask app
            self._instance._mongo.init_app(app, uri=MONGO_URI)
        except Exception as e:
            # If an error occurs during initialization, capture and report it to Sentry
            sentry_client.capture_exception(e)
