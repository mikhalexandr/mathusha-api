import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.String, default='')
    photo = sqlalchemy.Column(sqlalchemy.LargeBinary, default=None)
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
