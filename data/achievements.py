import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Achievement(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'achievements'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    user_achievement = orm.relationship(
        "UserAchievement",
        backref="achievement"
    )
