import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Achievement(SqlAlchemyBase):
    __tablename__ = 'achievements'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)
    unlocked = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    user_achievement = orm.relationship(
        "UserAchievement",
        backref="achievement"
    )
