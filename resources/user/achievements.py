from flask import g, jsonify, send_from_directory
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User


class AchievementsResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        res = []
        for achievement in user.achievements:
            res.append({
                'achievement_id': achievement.id,
                'name': achievement.name,
                'description': achievement.description,
                'photo': achievement.photo,
                'unlocked': achievement.unlocked
            })
        res = sorted(res, key=lambda x: x['unlocked'], reverse=True)
        return (jsonify(res),
                [send_from_directory('assets/achievements', f'{res[i]["photo"]}') for i in range(len(res))],
                200)
