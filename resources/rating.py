from flask_restful import Resource, abort


class RatingResource(Resource):
    @staticmethod
    def get():
        return "OK"