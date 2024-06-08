from flask_restful import Resource

from keycloak_integration import admin_required


class AdminStatisticsResource(Resource):
    @staticmethod
    @admin_required
    def get():
        pass
