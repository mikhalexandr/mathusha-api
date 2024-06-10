import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.String, default='default.jpg')
    rating = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    solved_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    ai_test = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    rating_trigger = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    topics = orm.relationship(
        "Topic",
        secondary="user_progress",
        backref="users"
    )

    achievements = orm.relationship(
        "Achievement",
        secondary="user_achievements",
        backref="users"
    )
