from flask import g, jsonify
from flask_restful import Resource

from keycloak_integration import authenticate
from misc import user_data_generation
from data import db_session
from data.users import User


class ProfileResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        if not user:
            user = User(
                id=g.user_id
            )
            session.add(user)
            user_data_generation(session, g.user_id)
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
            'username': user.username,
            'photo': user.photo,
            'rating': user.rating,
            'place_in_top': user_index + 1
        })
