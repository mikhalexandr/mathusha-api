from flask_restful import Resource


class ProfileResource(Resource):
    @staticmethod
    def get():
        return "OK"
