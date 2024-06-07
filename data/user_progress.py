import sqlalchemy

from .db_session import SqlAlchemyBase


class UserProgress(SqlAlchemyBase):
    __tablename__ = 'user_progress'

    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), primary_key=True)
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('topics.id'), primary_key=True)
    easy_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    medium_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    hard_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
