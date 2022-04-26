from app import flask_app
from google.cloud import error_reporting
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file('qwiklabs-gcp-00-92993ad3193b-897cb748b69b.json')
error_reporting_client = error_reporting.Client(credentials=credentials)

@flask_app.errorhandler(404)
def not_found(e):
    error_reporting_client.report(e)
    return 404

@flask_app.errorhandler(405)
def method_not_allowed(e):
    error_reporting_client.report(e)
    return 405

# @flask_app.errorhandler(500)
# def server_error(e):
#     error_reporting_client.report(e)
#     return 500
