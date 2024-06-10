from flask import g, request, send_from_directory
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User
from data.achievements import Achievement
from data.user_achievements import UserAchievement


class AchievementsResource(Resource):
    @staticmethod
    @authenticate
    def get():
        lang = request.args.get('lang', 'ru')
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
                'unlocked': user_achievement.unlocked
            })
        res = sorted(res, key=lambda x: x['unlocked'], reverse=True)
        return res, 200


class AchievementPhotoResource(Resource):
    @staticmethod
    @authenticate
    def get(achievement_id):
        session = db_session.create_session()
        achievement = session.query(Achievement).filter(Achievement.id == achievement_id).first()
        return send_from_directory('data/achievements', achievement.photo)
