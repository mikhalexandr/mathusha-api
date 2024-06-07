import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Topic(SqlAlchemyBase):
    __tablename__ = 'topics'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    tasks = orm.relationship(
        "Task",
        backref="topic"
    )

    users = orm.relationship(
        "User",
        secondary="user_progress",
        backref="topics"
    )
