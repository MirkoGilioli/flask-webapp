from app import flask_app

@flask_app.route('/')
def home():
    return 'Wecolme to Google Cloud DevOps!!!'

@flask_app.route('/dev')
def devPage():
    return 'Welcome this is the Development Page'

@flask_app.route('/about')
def devAbout():
    return 'Welcome this is the about Page'

@flask_app.route('/auth')
def devAuth():
    return 'Welcome this is the authentication Page'