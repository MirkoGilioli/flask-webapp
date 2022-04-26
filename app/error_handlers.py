from app import flask_app
from google.cloud import error_reporting


#error_reporting_client = error_reporting.Client()
# This handles page not found error
@flask_app.errorhandler(404)
def not_found(e):
    return 404
# This handles method not allowed
@flask_app.errorhandler(405)
def method_not_allowed(e):
    return 405

# @flask_app.errorhandler(500)
# def server_error(e):
#     error_reporting_client.report(e)
#     return 500
