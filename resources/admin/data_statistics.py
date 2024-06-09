from flask_restful import Resource

from keycloak_integration import admin_required
from data import db_session
from data.topics import Topic
from data.users import User
from data.achievements import Achievement


class AdminStatisticsResource(Resource):
    @staticmethod
    @admin_required
    def get():
        session = db_session.create_session()
        topics = session.query(Topic).all()
        topic_for_statistic = []
        for topic in topics:
            topic_for_statistic.append({
                'id': topic.id,
                'name': topic.name,
                'solved_tasks': topic.solved_tasks
            })
        topic_for_statistic = sorted(topic_for_statistic, key=lambda x: x['solved_tasks'], reverse=True)

        users = session.query(User).all()
        user_for_statistic = []
        for user in users:
            user_for_statistic.append({
                'id': user.id,
                'name': user.name,
                'solved_tasks': user.solved_tasks,
                'rating': user.rating
            })
        user_for_statistic = sorted(user_for_statistic, key=lambda x: (-x['solved_tasks'], -x['rating']))

        achievements = session.query(Achievement).all()
        achievement_for_statistic = []
        for ach in achievements:
            achievement_for_statistic.append({
                'id': ach.id,
                'name': ach.name,
                'solved_tasks': ach.taken
            })
        achievement_for_statistic = sorted(achievement_for_statistic, key=lambda x: x['solved_tasks'], reverse=True)

        return {
            'topics': topic_for_statistic,
            'users': user_for_statistic,
            'achievements': achievement_for_statistic
        }, 200
