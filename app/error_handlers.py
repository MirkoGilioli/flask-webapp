from unittest import case
from werkzeug.exceptions import HTTPException
from app import flask_app
from google.cloud import error_reporting

client = error_reporting.Client()

@flask_app.errorhandler(HTTPException)
def handle_exception(e):
    if e.code == 405:
        client.report("Method not allowed")