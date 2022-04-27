from app import flask_app
# Imports Python standard library logging
import logging

# This handles page not found error
@flask_app.errorhandler(404)
def not_found(e):
    # We send logging with severity ERROR to Cloud Log and Error Reporting
    logging.exception(e)

# This handles method not allowed
@flask_app.errorhandler(405)
def method_not_allowed(e):
    # We send logging with severity ERROR to Cloud Log and Error Reporting
    logging.exception(e)