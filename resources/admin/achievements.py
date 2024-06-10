from flask import request, send_from_directory
from flask_restful import Resource, abort
import os

from keycloak_integration import admin_required
from misc import allowed_file, allowed_file_size, translate
from data import db_session
from data.achievements import Achievement
from data.user_achievements import UserAchievement


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
        return res, 200


class AdminAchievementPhotoResource(Resource):
    @staticmethod
    @admin_required
    def get():
        achievement_id = request.json['id']
        session = db_session.create_session()
        achievements = session.query(Achievement).filter(Achievement.id == achievement_id).first()
        if achievements is None:
            abort(404, message="Achievements not found")
        return send_from_directory('assets/achievements', achievements.photo), 200


class AdminAchievementResource(Resource):
    @staticmethod
    @admin_required
    def patch():
        achievement_id = request.json['id']
        name = request.json['name']
        eng_name = translate(name, 'en')
        description = request.json['description']
        eng_description = translate(description, 'en')
        file = request.files['file']
        session = db_session.create_session()
        achievement = session.query(Achievement).filter(Achievement.id == achievement_id).first()
        if achievement is None:
            abort(404, message=f"Achievement with id [{achievement_id}] is not found")
        if achievement.name is not None:
            achievement.name = name
            achievement.eng_name = eng_name
        if achievement.description is not None:
            achievement.description = description
            achievement.eng_description = eng_description
        if file and allowed_file(file.filename) and allowed_file_size(file.content_length):
            os.remove(os.path.join('assets/achievements', achievement.photo))
            file.save(os.path.join('assets/achievements', achievement.photo))
        session.commit()
        return {"message": "OK"}, 200

    @staticmethod
    @admin_required
    def delete():
        achievement_id = request.json['id']
        session = db_session.create_session()
        achievement = session.query(Achievement).filter(Achievement.id == achievement_id).first()
        if achievement is None:
            abort(404, message=f"Topic with id [{achievement_id}] is not found")
        session.delete(achievement)
        achievements = session.query(UserAchievement).filter(UserAchievement.achievement_id == achievement_id).all()
        for ach in achievements:
            session.delete(ach)
        session.commit()
        return {"message": "OK"}, 200
