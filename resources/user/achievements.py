from flask import g, request, send_from_directory
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User
from data.user_achievements import UserAchievement


class AchievementsResource(Resource):
    @staticmethod
    @authenticate
    def get():
        lang = request.json['lang']
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        res = []
        for achievement in user.achievements:
            user_achievement = session.query(UserAchievement).filter(UserAchievement.user_id == g.user_id,
                                                            UserAchievement.achievement_id == achievement.id).first()
            res.append({
                'id': achievement.id,
                'name': achievement.name if lang == 'ru' else achievement.eng_name,
                'description': achievement.description if lang == 'ru' else achievement.eng_description,
                'photo': achievement.photo,
                'unlocked': user_achievement.unlocked
            })
        res = sorted(res, key=lambda x: x['unlocked'], reverse=True)
        return (res,
                [send_from_directory('assets/achievements', f'{res[i]["photo"]}') for i in range(len(res))],
                200)
