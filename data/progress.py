import sqlalchemy

from .db_session import SqlAlchemyBase


class Progress(SqlAlchemyBase):
    __tablename__ = 'progress'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user = sqlalchemy.orm.relationship('User')
    theme_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('themes.name'))
    theme = sqlalchemy.orm.relationship('Theme')
    level = sqlalchemy.Column(sqlalchemy.Integer)
    complexity = sqlalchemy.Column(sqlalchemy.Integer)
