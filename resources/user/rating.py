from flask import g, send_from_directory
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User


class RatingResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        users = session.query(User).all()
        rating = []
        h = 0
        for user in users:
            h += 1
            if h > 100:
                break
            rating.append({
                'id': user.id,
                'username': user.name,
                'rating': user.rating,
            })
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == g.user_id][0]
        user_info = rating[user_index], user_index + 1
        return {
            'rating': rating,
            'user_info': user_info,
        }, 200


class LeaderPhotoResource(Resource):
    @staticmethod
    @authenticate
    def get(leader_id):
        session = db_session.create_session()
        leader = session.query(User).filter(User.id == leader_id).first()
        return send_from_directory('assets/users', leader.photo)
