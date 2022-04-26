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