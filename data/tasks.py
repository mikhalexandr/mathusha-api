import sqlalchemy

from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('topics.id'))
    problem = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    solution = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    complexity = sqlalchemy.Column(sqlalchemy.Integer, default=1)
