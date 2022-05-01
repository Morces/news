from flask import Flask
from config import config_options
from app.requests import configure_request 

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # Registering the Blueprint
    from main import main as blue_print
    app.register_blueprint(blue_print)

    # Setting up configurations
    from requests import configure_request
    configure_request(app) 

    return app 
