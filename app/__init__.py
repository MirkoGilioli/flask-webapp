from flask import Flask
import google.cloud.logging

logging_client = google.cloud.logging.Client()
logging_client.setup_logging()


flask_app = Flask(__name__)

from app import routes
from app import error_handlers