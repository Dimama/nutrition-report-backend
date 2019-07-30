from os import environ

from flask import Flask, current_app
from flask_restful import Api
from flask_cors import CORS

from api.resources import Patient, Report
from db_wrapper import DBWrapper


def create_app():
    app = Flask(__name__)

    _ = CORS(app, resources={r"*": {"origins": "*"}})

    with app.app_context():
        current_app.db_wrapper = DBWrapper(environ['DB_HOST'], environ['DB_PORT'], environ['DATABASE'],
                                           environ['DB_USER'], environ['DB_PASSWORD'])

    api = Api(app)
    api.add_resource(Patient, "/patient")
    api.add_resource(Report, "/report")
    return app
