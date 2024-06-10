from flask import g, request
from flask_restful import Resource, abort
import random

from keycloak_integration import authenticate
from misc import list_of_generated_tasks, mixed_generation, yandex_gpt_setup
from data import db_session
from data.users import User
from data.user_progress import UserProgress
from data.topics import Topic
from data.tasks import Task
from data.achievements import Achievement
from data.user_achievements import UserAchievement
import consts


class TaskResource(Resource):
    @staticmethod
    @authenticate
    def get(topic_id):
        try:
            complexity = request.args.get('complexity', None)
            tasks_for_mix = request.args.get('tasks_for_mix', [])
            lang = request.args.get('lang', 'ru')
            session = db_session.create_session()
            if topic_id <= len(list_of_generated_tasks):
                return list_of_generated_tasks[topic_id - 1](complexity), 200
            elif topic_id == len(list_of_generated_tasks) + 1:
                if tasks_for_mix == 0:
                    abort(404, message=f"Tasks for mix [{tasks_for_mix}] are not found")
                return mixed_generation(complexity, tasks_for_mix)
            elif topic_id == len(list_of_generated_tasks) + 2:
                try:
                    return yandex_gpt_setup(lang), 200
                except Exception as e:
                    abort(404, message=f"Yandex GPT is unavailable now because of error [{e}]")
            else:
                topic_tasks = list(session.query(Task.problem, Task.solution).filter(Task.topic_id == topic_id,
                                                                                     Task.complexity == complexity).all())
                if len(topic_tasks) == 0:
                    abort(404, message=f"Tasks with topic_id [{topic_id}] and complexity [{complexity}] are not found")
                index = random.randint(0, len(topic_tasks) - 1)
                return {
                    'problem': topic_tasks[index][0],
                    'solution': topic_tasks[index][1]
                }, 200
        except Exception as e:
            return {'error': str(e)}, 404


class SolvedTaskResource(Resource):
    @staticmethod
    @authenticate
    def patch(topic_id):
        complexity = request.json['complexity']
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        user_progress = session.query(UserProgress).filter(UserProgress.user_id == g.user_id,
                                                           UserProgress.topic_id == topic_id).first()
        if topic_id == len(list_of_generated_tasks) + 2:
            user_progress.medium_solved_tasks += 1
            user.rating += 2
            if user.ai_test == 0:
                user.ai_test = 1
                achievement = session.query(Achievement).filter(Achievement.type == 0.0).first()
                achievement.taken += 1
                user_achievement = session.query(UserAchievement).filter(UserAchievement.user_id == g.user_id,
                                                            UserAchievement.achievement_id == achievement.id).first()
                user_achievement.unlocked = True
        elif complexity == 1:
            user_progress.easy_solved_tasks += 1
            user.rating += 1
        elif complexity == 2:
            user_progress.medium_solved_tasks += 1
            user.rating += 2
        elif complexity == 3:
            user_progress.hard_solved_tasks += 1
            user.rating += 3
        user.solved_tasks += 1
        if user.solved_tasks in consts.solved_tasks_amount:
            tmp = float(f'2.{str(consts.solved_tasks_amount.index(user.solved_tasks) + 1)}')
            achievement = session.query(Achievement).filter(Achievement.type == tmp).first()
            user_achievement = session.query(UserAchievement).filter(UserAchievement.user_id == g.user_id,
                                                            UserAchievement.achievement_id == achievement.id).first()
            if not user_achievement.unlocked:
                user_achievement.unlocked = True
                achievement.taken += 1
        topic = session.query(Topic).filter(Topic.id == topic_id).first()
        topic.solved_tasks += 1
        session.commit()
        return {"message": "OK"}, 200
