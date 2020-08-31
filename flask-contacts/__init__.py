from flask_restful import Api
from flask import Flask
from flask_alchemy import SQLAlchemy

db = SQLAlchemy()

# Instance DB
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app)
    db.init(api)