import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Topic(SqlAlchemyBase):
    __tablename__ = 'topics'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    eng_name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.String, default='default.jpg')
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    eng_description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    color = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    tasks = orm.relationship(
        "Task",
        backref="topic"
    )
