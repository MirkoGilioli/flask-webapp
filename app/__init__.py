from flask import Flask
from app import routes
from app import error_handlers

flask_app = Flask(__name__)