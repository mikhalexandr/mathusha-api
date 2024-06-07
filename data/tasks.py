import sqlalchemy

from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('topics.id'))
    problem = sqlalchemy.Column(sqlalchemy.String)
    solution = sqlalchemy.Column(sqlalchemy.String)
    complexity = sqlalchemy.Column(sqlalchemy.Integer)
