from flask import g, request
from flask_restful import Resource

from keycloak_integration import authenticate
from data import db_session
from data.users import User
from data.user_progress import UserProgress


class ProgressResource(Resource):
    @staticmethod
    @authenticate
    def get():
        lang = request.json['lang']
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        res = []
        for topic_progress in user.topics:
            user_progress = session.query(UserProgress).filter(UserProgress.user_id == g.user_id,
                                                               UserProgress.topic_id == topic_progress.id).first()
            res.append({
                'id': topic_progress.id,
                'name': topic_progress.name if lang == 'ru' else topic_progress.eng_name,
                'color': topic_progress.color,
                'easy_solved_tasks': user_progress.easy_solved_tasks,
                'medium_solved_tasks': user_progress.medium_solved_tasks,
                'hard_solved_tasks': user_progress.hard_solved_tasks,
                'solved_tasks': (user_progress.easy_solved_tasks + user_progress.medium_solved_tasks
                                 + user_progress.hard_solved_tasks)
            })
        return res, 200
