from flask import g, jsonify, request, send_from_directory
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User


class AchievementsResource(Resource):
    @staticmethod
    @authenticate
    def get():
        lang = request.json['lang']
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        res = []
        for achievement in user.achievements:
            res.append({
                'id': achievement.id,
                'name': achievement.name if lang == 'ru' else achievement.eng_name,
                'description': achievement.description if lang == 'ru' else achievement.eng_description,
                'photo': achievement.photo,
                'unlocked': achievement.unlocked
            })
        res = sorted(res, key=lambda x: x['unlocked'], reverse=True)
        return (jsonify(res),
                [send_from_directory('assets/achievements', f'{res[i]["photo"]}') for i in range(len(res))],
                200)
