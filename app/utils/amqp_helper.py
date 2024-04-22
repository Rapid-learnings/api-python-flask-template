import os

import pika
from dotenv import load_dotenv

from config import logger

# Load environment variables from a .env file
load_dotenv()


# AMQPHelper class for interacting with RabbitMQ
class AMQPHelper:

    def __init__(self, exchange_name):
        # Get the RabbitMQ broker URL from environment variables
        self.amqp_url = os.getenv("RABBITMQ_BROKER_URL")
        self.exchange_name = exchange_name
        self.connection = None
        self.channel = None
        self.connect()  # Establish a connection on object initialization

    def connect(self):
        try:
            # Establish a connection to the RabbitMQ server
            self.connection = pika.BlockingConnection(pika.URLParameters(self.amqp_url))
            self.channel = self.connection.channel()

            # Declare the exchange if it doesn't exist
            self.channel.exchange_declare(
                exchange=self.exchange_name, exchange_type="fanout"
            )

            logger.info("Connected to RabbitMQ server.")
        except Exception as e:
            logger.error(f"Failed to connect to RabbitMQ server: {str(e)}")
            raise

    def publish(self, routing_key, message, durable=False):
        try:
            logger.info(message)

            # Publish the message to the exchange with the specified routing key
            self.channel.basic_publish(
                exchange=self.exchange_name,
                routing_key=routing_key,
                body=message,
                properties=pika.BasicProperties(content_type="text/plain"),
            )

        except Exception as e:
            logger.error(f"Failed to publish message: {str(e)}")
            raise
        finally:
            # Disconnect after publishing the message
            self.disconnect()

    def disconnect(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            logger.info("Disconnected from RabbitMQ server.")
        else:
            logger.info("Already disconnected.")
