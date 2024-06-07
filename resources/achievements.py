from flask_restful import Resource


class AchievementsListResource(Resource):
    @staticmethod
    def get():
        return "OK"
