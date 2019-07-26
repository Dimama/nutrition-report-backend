from http import HTTPStatus

from flask_restful import Resource, reqparse
from flask import current_app, request


class Report(Resource):

    post_parser = reqparse.RequestParser()

    def post(self):
        current_app.logger.debug(request.data)

        return {"message": "OK"}, HTTPStatus.CREATED
