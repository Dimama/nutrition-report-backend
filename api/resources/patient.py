from http import HTTPStatus

from flask_restful import Resource, reqparse
from flask import current_app, request


class Patient(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument("name", type=str, required=True, location="json")

    @staticmethod
    def get():
        patients = current_app.db_wrapper.get_patients()

        return {"patients": patients}, HTTPStatus.OK

    def post(self):
        current_app.logger.debug(request.data)

        data = self.post_parser.parse_args()
        patient = current_app.db_wrapper.add_patient(data["name"])

        if patient:
            return {"message": "patient added"}, HTTPStatus.CREATED
        else:
            return {"message": "server error"}, HTTPStatus.INTERNAL_SERVER_ERROR
