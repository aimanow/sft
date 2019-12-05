import os
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from godmode.database import database

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///database/demo.sqlite")

# pg_database = database("sqlite:///database/demo.sqlite", connect_args={"check_same_thread": False})
pg_database = database(DATABASE_URI)

class User(pg_database.TableBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, name='id', primary_key=True)
    fullname = sa.Column(sa.VARCHAR, name='fullname')
    avatar_path = sa.Column(sa.VARCHAR, name='avatar_path')
    registered_at = sa.Column(sa.TIMESTAMP, name='registered_at')

# class Temp(db.TableBase):
#     __table__ = sa.Table('temp', db.metadata, autoload=True)
#
#     user = relationship('User')
