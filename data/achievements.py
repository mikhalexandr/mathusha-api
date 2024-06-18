import sqlalchemy

from .db_session import SqlAlchemyBase


class Achievement(SqlAlchemyBase):
    __tablename__ = 'achievements'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    eng_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.String, default='default.jpg')
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    eng_description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    taken = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    type = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    # 1 - place in top, 2 - amount of solved tasks, 3 - rating
