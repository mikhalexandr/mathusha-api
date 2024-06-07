from flask import g, jsonify, request, send_file
from flask_restful import Resource, abort
from werkzeug.utils import secure_filename
import io

from keycloak_integration import authenticate
from data import db_session
from data.users import User


class ProfileResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        current_user = session.query(User).filter(User.id == g.user_id).first()
        users = list(session.query(User).all())
        rating = []
        for user in users:
            rating.append({
                'id': user.id,
                'rating': user.rating,
            })
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == g.user_id][0]
        return jsonify({
            'username': current_user.username,
            'photo': send_file((io.BytesIO(current_user.photo))) if current_user.photo else None,
            'rating': current_user.rating,
            'place_in_top': user_index + 1
        }), 200


class ProfilePhotoResource(Resource):
    @staticmethod
    @authenticate
    def patch():
        if 'file' not in request.files:
            abort(400, message="No file part")
        file = request.files['file']
        if file.filename == '':
            abort(400, message="No selected file")
        filename = secure_filename(file.filename)
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            abort(415, message="Invalid file type")
        file_data = file.read()
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        user.photo = file_data
        session.commit()
        return jsonify({"message": "OK"}), 200

    @staticmethod
    @authenticate
    def delete():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        user.photo = None
        session.commit()
        return jsonify({"message": "OK"}), 200
