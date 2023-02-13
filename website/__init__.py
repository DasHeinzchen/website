from flask import Flask
from website.config import Config


def create_app(config_class=Config):
    app = Flask
    app.config.from_object(Config)

    return app
