import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class UserAchievement(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user_achievements'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"), nullable=False)
    achievement_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("achievements.id"), nullable=False)
    unlocked = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
