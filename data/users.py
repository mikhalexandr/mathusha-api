import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.String, default='assets/default.jpg')
    rating = sqlalchemy.Column(sqlalchemy.Integer, default=0)

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
