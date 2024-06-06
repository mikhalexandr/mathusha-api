import sqlalchemy

from .db_session import SqlAlchemyBase


class Progress(SqlAlchemyBase):
    __tablename__ = 'progress'

    easy_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    medium_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    hard_solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'))
    topic_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('topics.id'))
