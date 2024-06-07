from flask_restful import Resource


class ProgressListResource(Resource):
    @staticmethod
    def get():
        return "OK"
