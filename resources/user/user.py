from flask import g, jsonify, request, send_from_directory
from flask_restful import Resource, abort
from werkzeug.utils import secure_filename
import os

from keycloak_integration import authenticate
from misc import allowed_file, allowed_file_size
from data import db_session
from data.users import User


class UserResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        current_user = session.query(User).filter(User.id == g.user_id).first()
        users = session.query(User).all()
        rating = []
        for user in users:
            rating.append({
                'id': user.id,
                'rating': user.rating,
            })
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == g.user_id][0]
        return jsonify({
            'username': current_user.name,
            'rating': current_user.rating,
            'place_in_top': user_index + 1
        }), send_from_directory('assets/users', f'{current_user.photo}'), 200


class UserPhotoResource(Resource):
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
        return jsonify({"message": "OK"}), 200

    @staticmethod
    @authenticate
    def delete():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        os.remove(user.photo)
        user.photo = 'assets/users/default.jpg'
        session.commit()
        return jsonify({"message": "OK"}), 200
