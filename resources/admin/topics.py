from flask import request, send_from_directory
from flask_restful import Resource, abort
from werkzeug.utils import secure_filename
from sqlalchemy import func
import os

from keycloak_integration import admin_required
from misc import list_of_generated_tasks, allowed_file, allowed_file_size, allowed_excel_file, excel_to_db, translate
from data import db_session
from data.topics import Topic
from data.users import User
from data.user_progress import UserProgress


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
        return res, 200


class AdminTopicPhotoResource(Resource):
    @staticmethod
    @admin_required
    def get():
        topic_id = request.json['id']
        session = db_session.create_session()
        topics = session.query(Topic).filter(Topic.id == topic_id).first()
        if topics is None:
            abort(404, message="Topics not found")
        return send_from_directory('assets/topics', topics.photo), 200


class AdminTopicResource(Resource):
    @staticmethod
    @admin_required
    def post():
        if 'file' not in request.files or 'excel_file' not in request.files:
            abort(400, message="No file part")
        name = request.json['name']
        eng_name = translate(name, 'en')
        description = request.json['description']
        eng_description = translate(description, 'en')
        file = request.files['file']
        excel_file = request.files['excel_file']
        if file.filename == '' or excel_file.filename == '':
            abort(400, message="No selected file")
        session = db_session.create_session()
        count = session.query(func.count()).select_from(Topic).scalar()
        filename = None
        if file and allowed_file(file.filename) and allowed_file_size(file.content_length):
            filename = f'{count + 1}.{secure_filename(file.filename).split(".")[1]}'
            file.save(os.path.join('assets/topics', filename))
        else:
            abort(400, message="File is incorrect")
        if allowed_excel_file(excel_file.filename):
            fn = f'adding_theme.{secure_filename(excel_file.filename).split(".")[1]}'
            excel_file.save(os.path.join('assets/topics', fn))
            excel_to_db(session, f'assets/{fn}', name, eng_name, description, eng_description, filename,
                        count + 1)
        else:
            abort(400, message="Excel file is incorrect")
        users = session.query(User.id).all()
        for user in users:
            user_progress = UserProgress(
                user_id=user.id,
                topic_id=count + 1
            )
            session.add(user_progress)
        session.commit()
        return {"message": "OK"}, 200

    @staticmethod
    @admin_required
    def patch():
        topic_id = request.json['id']
        name = request.json['name']
        description = request.json['description']
        file = request.files['file']
        session = db_session.create_session()
        topic = session.query(Topic).filter(Topic.id == topic_id).first()
        if topic is None:
            abort(404, message=f"Topic with id [{topic_id}] is not found")
        if name is not None:
            topic.name = name
        if description is not None:
            topic.description = description
        if file and allowed_file(file.filename) and allowed_file_size(file.content_length):
            os.remove(os.path.join('assets/topics', topic.photo))
            file.save(os.path.join('assets/topics', topic.photo))
        session.commit()
        return {"message": "OK"}, 200

    @staticmethod
    @admin_required
    def delete():
        topic_id = request.json['id']
        if topic_id < len(list_of_generated_tasks) + 2:
            abort(400, message=f"Topic with id [{topic_id}] can't be deleted")
        session = db_session.create_session()
        topic = session.query(Topic).filter(Topic.id == topic_id).first()
        if topic is None:
            abort(404, message=f"Topic with id [{topic_id}] is not found")
        session.delete(topic)
        progress = session.query(UserProgress).filter(UserProgress.topic_id == topic_id).all()
        for prog in progress:
            session.delete(prog)
        session.commit()
        return {"message": "OK"}, 200
