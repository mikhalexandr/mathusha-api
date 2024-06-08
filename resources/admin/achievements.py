from flask import jsonify, send_from_directory
from flask_restful import Resource, abort

from keycloak_integration import admin_required
from data import db_session
from data.achievements import Achievement


class AdminAchievementsResource(Resource):
    @staticmethod
    @admin_required
    def get():
        session = db_session.create_session()
        achievements = session.query(Achievement).all()
        if achievements is None:
            abort(404, message="Achievements not found")
        res = []
        for ach in achievements:
            res.append({
                'id': ach.id,
                'name': ach.name,
                'description': ach.description
            })
        return (jsonify(res),
                [send_from_directory('assets/achievements', f'{ach.photo}') for ach in achievements],
                200)


class AdminAchievementResource(Resource):
    @staticmethod
    @admin_required
    def post():
        pass
