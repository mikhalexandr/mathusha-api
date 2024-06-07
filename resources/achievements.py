from flask import g, jsonify
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.user_achievements import UserAchievement


class AchievementsListResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        user_achievements = session.query(UserAchievement).filter(UserAchievement.user_id == g.user_id).all()
        res = []
        for i in user_achievements:
            res.append({
                'achievement_id': i.achievement_id,
                'unlocked': i.unlocked
            })
        return jsonify(res), 200
