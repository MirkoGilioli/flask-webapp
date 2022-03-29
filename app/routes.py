from app import app

@app.route('/')
def home():
    return 'Wecolme to Google Cloud DevOps!'