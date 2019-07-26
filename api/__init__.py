from flask import Flask, current_app
from flask_restful import Api
from flask_cors import CORS
from api.resources import Patient
from db_wrapper import DBWrapper

from config import DB_FILENAME


def create_app():
    app = Flask(__name__)

    _ = CORS(app, resources={r"*": {"origins": "*"}})

    with app.app_context():
        current_app.db_wrapper = DBWrapper(DB_FILENAME)

    api = Api(app)
    api.add_resource(Patient, "/patient")

    return app
