import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.String)
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    rating = sqlalchemy.Column(sqlalchemy.Float, default=0)

    user_progress = orm.relationship(
        "UserProgress",
        backref="user"
    )

    user_achievements = orm.relationship(
        "UserAchievement",
        backref="user"
    )
