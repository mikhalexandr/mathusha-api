from flask import g, jsonify, request
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User


class ProgressResource(Resource):
    @staticmethod
    @authenticate
    def get():
        lang = request.json['lang']
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        res = []
        for topic_progress in user.topics:
            res.append({
                'id': topic_progress.id,
                'topic_name': topic_progress.name if lang == 'ru' else topic_progress.eng_name,
                'topic_color': topic_progress.color,
                'easy_solved_tasks': topic_progress.easy_solved_tasks,
                'medium_solved_tasks': topic_progress.medium_solved_tasks,
                'hard_solved_tasks': topic_progress.hard_solved_tasks,
                'solved_tasks': (topic_progress.easy_solved_tasks + topic_progress.medium_solved_tasks
                                 + topic_progress.hard_solved_tasks),
                'color': topic_progress.color
            })
        return jsonify(res), 200
