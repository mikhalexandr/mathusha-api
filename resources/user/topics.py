from flask import g, jsonify, request, send_from_directory
from flask_restful import Resource, abort

from keycloak_integration import authenticate
from misc import user_data_generation
from data import db_session
from data.users import User
from data.topics import Topic


class TopicsResource(Resource):
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
        res = []
        topics = session.query(Topic).all()
        if topics is None:
            abort(404, message="Topics not found")
        for topic in topics:
            res.append({
                'id': topic.id,
                'name': topic.name,
                'photo': topic.photo,
            })
        session.commit()
        return (
            jsonify(res),
            [send_from_directory('assets/topics', f'{topic.photo}') for topic in topics],
            200
        )


class TopicDescriptionResource(Resource):
    @staticmethod
    @authenticate
    def get():
        topic_id = request.json['topic_id']
        session = db_session.create_session()
        topic = session.query(Topic).filter(Topic.id == topic_id).first()
        if topic is None:
            abort(404, message=f"Topic with id [{topic_id}] is not found")
        return jsonify({
            'description': topic.description
        }), 200
