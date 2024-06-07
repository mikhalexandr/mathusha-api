from flask import g, jsonify
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User


class RatingResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        users = list(session.query(User).all())
        rating = []
        for user in users:
            d = {
                'id': user.id,
                'username': user.username,
                'photo': user.photo,
                'rating': user.rating,
            }
            rating.append(d)
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == g.user_id][0]
        user_info = rating[user_index], user_index + 1
        return jsonify({
            'rating': rating,
            'user_info': user_info
        })
