from flask import g, request, send_from_directory
from flask_restful import Resource, abort
from werkzeug.utils import secure_filename
import os

from keycloak_integration import authenticate
from misc import allowed_file, allowed_file_size
from data import db_session
from data.users import User
from data.achievements import Achievement
from data.user_achievements import UserAchievement


class UserResource(Resource):
    @staticmethod
    @authenticate
    def get():
        user_id = request.json['id']
        session = db_session.create_session()
        current_user = session.query(User).filter(User.id == user_id).first()
        users = session.query(User).all()
        rating = []
        for user in users:
            rating.append({
                'id': user.id,
                'rating': user.rating,
            })
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == user_id][0]
        if 0 < user_index + 1 < 4:
            tmp = float(f'1.{user_index + 1}')
            achievement = session.query(Achievement).filter(Achievement.type == tmp).first()
            user_ach = session.query(UserAchievement).filter(UserAchievement.user_id == user_id,
                                                             UserAchievement.achievement_id == achievement.id).first()
            if not user_ach.unlocked:
                user_ach.unlocked = True
                achievement.taken += 1
                session.commit()
        return {
            'username': current_user.name,
            'rating': current_user.rating,
            'place_in_top': user_index + 1
        }, 200


class UserPhotoResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        return send_from_directory('assets/users', user.photo)

    @staticmethod
    @authenticate
    def put():
        if 'file' not in request.files:
            abort(400, message="No file part")
        file = request.files['file']
        if file.filename == '':
            abort(400, message="No selected file")
        filename = None
        if file and allowed_file(file.filename) and allowed_file_size(file.content_length):
            filename = f'{g.user_id}.{secure_filename(file.filename).split(".")[1]}'
            file.save(os.path.join('assets/users', filename))
        else:
            abort(400, message="File is incorrect")
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        user.photo = 'assets/users/' + filename
        session.commit()
        return {"message": "OK"}, 200

    @staticmethod
    @authenticate
    def delete():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        os.remove(user.photo)
        user.photo = 'assets/users/default.jpg'
        session.commit()
        return {"message": "OK"}, 200
