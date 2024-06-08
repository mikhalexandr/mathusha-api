from flask import jsonify, send_from_directory
from flask_restful import Resource, abort

from keycloak_integration import admin_required
from data import db_session
from data.topics import Topic


class AdminTopicsResource(Resource):
    @staticmethod
    @admin_required
    def get():
        session = db_session.create_session()
        topics = session.query(Topic).all()
        if topics is None:
            abort(404, message="Topics not found")
        res = []
        for topic in topics:
            res.append({
                'id': topic.id,
                'name': topic.name,
                'description': topic.description
            })
        return (jsonify(res),
                [send_from_directory('assets/topics', f'{topic.photo}') for topic in topics],
                200)


class AdminTopicResource(Resource):
    pass
