import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class TopicExpression(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'topic_expressions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    problem = sqlalchemy.Column(sqlalchemy.String)
    solution = sqlalchemy.Column(sqlalchemy.String)
    complexity = sqlalchemy.Column(sqlalchemy.Integer)
    topic_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('topics.name'))

    topic = orm.relationship(
        "Topic",
        backref="topic_expression"
    )
