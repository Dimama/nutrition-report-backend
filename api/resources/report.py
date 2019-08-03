from http import HTTPStatus

from flask_restful import Resource, reqparse
from flask import current_app, request


class Report(Resource):

    root_post_parser = reqparse.RequestParser()
    post_parser = reqparse.RequestParser()

    root_post_parser.add_argument("data", type=dict, required=True, location="json")
    post_parser.add_argument("patient", type=str, required=True, location=("data",))
    post_parser.add_argument("dateFrom", type=str, required=True, location=("data",))
    post_parser.add_argument("dateTo", type=str, required=True, location=("data",))
    post_parser.add_argument("stool", type=str, required=True, location=("data",))
    post_parser.add_argument("vomit", type=str, required=True, location=("data",))
    post_parser.add_argument("appetite", type=str, required=True, location=("data",))
    post_parser.add_argument("mucositis", type=str, required=True, location=("data",))
    post_parser.add_argument("nausea", type=str, required=True, location=("data",))
    post_parser.add_argument("ration", type=str, required=True, location=("data",))
    post_parser.add_argument("sipping", type=dict, action="append", required=True, location=("data",))
    post_parser.add_argument("EN", type=dict, action="append",  required=True, location=("data",))
    post_parser.add_argument("components", type=str, required=True, location=("data",))
    post_parser.add_argument("interval", type=str, required=True, location=("data",))
    post_parser.add_argument("needs", type=str, required=True, location=("data",))
    post_parser.add_argument("doctor", type=str, required=True, location=("data",))

    def post(self):
        current_app.logger.debug(request.data)

        record = self.post_parser.parse_args(self.root_post_parser.parse_args())
        try:
            current_app.db_wrapper.add_record(record)
        except Exception as e:
            current_app.logger.error(e)
            return {"message": "server error"}, HTTPStatus.INTERNAL_SERVER_ERROR

        return {"message": "record added"}, HTTPStatus.CREATED
