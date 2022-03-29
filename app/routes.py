from app import flask_app

@flask_app.route('/')
def home():
    return 'Wecolme to Google Cloud DevOps!'