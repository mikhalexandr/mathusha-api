from flask import g, request, send_from_directory
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
        list_leaders = []
        if len(rating) == 1:
            leader = rating[0]
            list_leaders.append(leader['id'])
        elif len(rating) == 2:
            leader1, leader2 = rating[0], rating[1]
            list_leaders.append(leader1['id'])
            list_leaders.append(leader2['id'])
        else:
            leader1, leader2, leader3 = rating[0], rating[1], rating[2]
            list_leaders.append(leader1['id'])
            list_leaders.append(leader2['id'])
            list_leaders.append(leader3['id'])
        leaders = list((session.query(User.id, User.name).filter
                   (User.id.in_([i for i in list_leaders])).all()))
        leaders_info = []
        for leader in leaders:
            leaders_info.append({
                'id': leader[0],
                'username': leader[1],
            })
        return {
            'rating': rating,
            'user_info': user_info,
            'leaders': leaders_info,
        }, 200


class LeaderPhotoResource(Resource):
    @staticmethod
    @authenticate
    def get(leader_id):
        session = db_session.create_session()
        leader = session.query(User).filter(User.id == leader_id).first()
        return send_from_directory('assets/users', leader.photo)
