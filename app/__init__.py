from flask import Flask
# Imports the Cloud Logging client library
import google.cloud.logging

logging_client = google.cloud.logging.Client()
# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
logging_client.setup_logging()


flask_app = Flask(__name__)

from app import routes
from app import error_handlers