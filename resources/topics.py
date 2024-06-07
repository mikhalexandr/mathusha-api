from flask_restful import Resource
from flask import g, jsonify

from keycloak_integration import authenticate
from data import db_session
from data.users import User
from data.topics import Topic


class TopicListResource(Resource):
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
        res = []
        topics = session.query(Topic).all()
        for i in topics:
            d = {
                'id': i.id,
                'name': i.name,
                'image': i.image,
            }
            res.append(d)
        return jsonify(res)
