from app import flask_app

@flask_app.route('/')
def home():
    return 'Wecolme to Google Cloud DevOps!'

@flask_app.route('/dev')
def devPage():
    return 'Welcome this is the Development Page'

@flask_app.route('/health')
def healthPage():
    return 'The application is healthy'