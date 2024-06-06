import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Topic(SqlAlchemyBase):
    __tablename__ = 'topics'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    generator_id = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    progress = orm.relationship(
        "Progress",
        backref="topic"
    )
