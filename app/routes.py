from time import sleep
from app import flask_app

@flask_app.route('/')
def home():
    a=5
    b=3
    c = a + b
    print (c)
    return 'Wecolme to Google Cloud DevOps!!!'

@flask_app.route('/dev')
def dev():
    return 'Welcome this is the Development Page'

@flask_app.route('/about')
def about():
    sleep(5)
    return 'Welcome this is the about Page'

@flask_app.route('/auth')
def auth():
    return 'Welcome this is the authentication Page'

@flask_app.route('/help')
def help():
    return 'Welcome this is the help Page'

@flask_app.route('/orders')
def orders():
    return 'Welcome this is the orders Page'

@flask_app.route('/inventory')
def inventory():
    return 'Welcome this is the inventory Page'

@flask_app.route('/devClass')
def devClass():
    return 'Welcome this is the GCP Dev Class Page'

@flask_app.route('/example')
def example():
    return 'Welcome this is the example Page'

@flask_app.route('/example2')
def example2():
    return 'Welcome this is the example2 Page'