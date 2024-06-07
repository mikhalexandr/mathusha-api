from flask import g, jsonify
from flask_restful import Resource

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
            d = {
                'id': user.id,
                'rating': user.rating,
            }
            rating.append(d)
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == g.user_id][0]
        return jsonify({
            'username': current_user.username,
            'photo': current_user.photo,
            'rating': current_user.rating,
            'place_in_top': user_index + 1
        })


class ProfilePhotoResource(Resource):
    @staticmethod
    @authenticate
    def post():
        pass

    @staticmethod
    @authenticate
    def patch():
        pass

    @staticmethod
    @authenticate
    def delete():
        pass
