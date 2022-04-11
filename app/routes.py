from app import flask_app

@flask_app.route('/')
def home():
    return 'Wecolme to Google Cloud DevOps!!!'

@flask_app.route('/dev')
def dev():
    return 'Welcome this is the Development Page'

@flask_app.route('/about')
def about():
    return 'Welcome this is the about Page'

@flask_app.route('/auth')
def auth():
    return 'Welcome this is the authentication Page'