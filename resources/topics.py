from flask import g, jsonify, request, send_file
from flask_restful import Resource, abort
import io

from keycloak_integration import authenticate
from misc import user_data_generation
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
            user_data_generation(session, g.user_id)
        res = []
        topics = session.query(Topic).all()
        if topics is None:
            abort(404, message="Topics not found")
        for i in topics:
            d = {
                'id': i.id,
                'name': i.name,
                'image': send_file((io.BytesIO(i.image))) if i.image else None,
            }
            res.append(d)
        session.commit()
        return jsonify(res), 200


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
