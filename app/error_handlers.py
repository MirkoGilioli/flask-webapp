from app import flask_app
from google.cloud import logging
import logging

logging_client = logging.Client()
logging_client.setup_logging()

# This handles page not found error
@flask_app.errorhandler(404)
def not_found(e):
    logging.exception(e)
    return 404
# This handles method not allowed
@flask_app.errorhandler(405)
def method_not_allowed(e):
    logging.exception(e)
    return 405

# @flask_app.errorhandler(500)
# def server_error(e):
#     error_reporting_client.report(e)
#     return 500
