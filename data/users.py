import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.String)
    photo = sqlalchemy.Column(sqlalchemy.String)
    rating = sqlalchemy.Column(sqlalchemy.Float)

    progress = orm.relationship(
        "Progress",
        backref="user"
    )

    achievements = orm.relationship(
        "Achievement",
        backref="user"
    )
