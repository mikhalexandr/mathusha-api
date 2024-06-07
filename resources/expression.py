from flask_restful import Resource, abort
from flask import g, request, jsonify
import random

from keycloak_integration import authenticate
from misc import list_of_expressions, mixed_generation, yandex_gpt_setup
from data import db_session
from data.users import User
from data.user_progress import UserProgress
from data.topics import Topic
from data.topic_expressions import TopicExpression


class ExpressionGetResource(Resource):
    @staticmethod
    @authenticate
    def get():
        try:
            id_ = request.json['id']
            complexity = request.json['complexity']
            session = db_session.create_session()
            if id_ <= len(list_of_expressions):
                return jsonify(list_of_expressions[id_ - 1](complexity))
            elif id_ == len(list_of_expressions) + 1:
                return jsonify(mixed_generation(complexity))
            elif id_ == len(list_of_expressions) + 2:
                return jsonify(yandex_gpt_setup())
            else:
                topic = session.query(Topic).filter(Topic.id == id_).first()
                if topic is None:
                    abort(404, message=f"Topic with id [{id_}] is not found")
                topic_expressions = list(session.query(TopicExpression).filter(TopicExpression.topic_id == id_,
                                                                          TopicExpression.complexity == complexity).all())
                index = random.randint(0, len(topic_expressions) - 1)
                return jsonify({
                    'problem': topic_expressions[index]['problem'],
                    'solution': topic_expressions[index]['solution']
                })
        except Exception as e:
            return jsonify({'error': str(e)})


class ExpressionPostResource(Resource):
    @staticmethod
    def patch():
        id_ = request.json['id']
        complexity = request.json['complexity']
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        user_progress = session.query(UserProgress).filter(UserProgress.user_id == g.user_id,
                                                           UserProgress.topic_id == id_).first()
        if complexity == 1:
            user_progress.easy_solved_tasks += 1
            user.rating += 1
        elif complexity == 2:
            user_progress.medium_solved_tasks += 1
            user.rating += 2
        elif complexity == 3:
            user_progress.hard_solved_tasks += 1
            user.rating += 3
        session.commit()
        return jsonify({"message": "OK"})
