import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class ThemeExpression(SqlAlchemyBase):
    __tablename__ = 'themes_expressions'

    problem = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    solution = sqlalchemy.Column(sqlalchemy.String)
    complexity = sqlalchemy.Column(sqlalchemy.Integer)
    theme_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('themes.name'))

    theme = orm.relationship(
        "Theme",
        backref="theme_expressions"
    )
