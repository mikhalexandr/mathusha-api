import sqlalchemy

from .db_session import SqlAlchemyBase


class Theme(SqlAlchemyBase):
    __tablename__ = 'themes'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)