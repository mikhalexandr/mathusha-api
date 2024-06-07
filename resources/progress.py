from flask import g, jsonify
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.user_progress import UserProgress


class ProgressListResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        user_progress = session.query(UserProgress).filter(UserProgress.user_id == g.user_id).all()
        res = []
        for i in user_progress:
            d = {
                'topic_id': i.topic_id,
                'easy_solved_tasks': i.easy_solved_tasks,
                'medium_solved_tasks': i.medium_solved_tasks,
                'hard_solved_tasks': i.hard_solved_tasks,
                'all_solved_tasks': i.easy_solved_tasks + i.medium_solved_tasks + i.hard_solved_tasks
            }
            res.append(d)
        return jsonify(res)
