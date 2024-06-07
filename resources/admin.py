from flask_restful import Resource


class AddThemeResource(Resource):
    @staticmethod
    def post():
        return "OK"


class DeleteThemeResource(Resource):
    @staticmethod
    def delete():
        return "OK"


class UpdateThemeResource(Resource):
    @staticmethod
    def patch():
        return "OK"


class DeleteAchievementResource(Resource):
    @staticmethod
    def delete():
        return "OK"


class UpdateAchievementResource(Resource):
    @staticmethod
    def patch():
        return "OK"
