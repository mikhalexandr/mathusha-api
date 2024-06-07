from flask_restful import Resource


class ExpressionGetResource(Resource):
    @staticmethod
    def get():
        return "OK"


class ExpressionPostResource(Resource):
    @staticmethod
    def post():
        return "OK"
