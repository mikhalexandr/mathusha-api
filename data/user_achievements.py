import sqlalchemy

from .db_session import SqlAlchemyBase


class UserAchievement(SqlAlchemyBase):
    __tablename__ = 'user_achievements'

    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"), primary_key=True)
    achievement_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("achievements.id"), primary_key=True)
    unlocked = sqlalchemy.Column(sqlalchemy.Integer, default=0)
