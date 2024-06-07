from flask import g, jsonify, send_file
from flask_restful import Resource
import io

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
        for user in users:
            d = {
                'id': user.id,
                'username': user.username,
                'rating': user.rating,
            }
            rating.append(d)
        rating = sorted(rating, key=lambda x: x['rating'], reverse=True)
        user_index = [x for x in range(len(rating)) if rating[x]["id"] == g.user_id][0]
        user_info = rating[user_index], user_index + 1
        leader1, leader2, leader3 = rating[0], rating[1], rating[2]
        leaders = (session.query(User.id, User.photo).filter
                   (User.id.in_([leader1['id'], leader2['id'], leader3['id']])).all())
        leaders_info = []
        for leader in leaders:
            leaders_info.append({
                'id': leader[0],
                'photo': send_file((io.BytesIO(leader[1]))) if leader[1] else None
            })
        return jsonify({
            'leaders': leaders_info,
            'rating': rating[3:],
            'user_info': user_info
        }), 200
