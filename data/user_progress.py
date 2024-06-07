import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class UserProgress(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user_progress'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    easy_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    medium_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    hard_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'))
    topic_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('topics.id'))
