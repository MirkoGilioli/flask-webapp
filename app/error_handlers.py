from app import flask_app
from app import error_reporting_client

@flask_app.errorhandler(404)
def not_found(e):
    error_reporting_client.report(e)

@flask_app.errorhandler(405)
def method_not_allowed(e):
    error_reporting_client.report(e)