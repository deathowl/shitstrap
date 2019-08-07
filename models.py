from sqlalchemy import ForeignKey, Column, String, Integer, Boolean
from sqlalchemy import true as db_true
from sqlalchemy import false as db_false
from sqlalchemy.event import listens_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from db import db

Base = declarative_base()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = Column(db.Integer(), primary_key=True)
    email = Column(String(30), unique=True, nullable=False)
    name = Column(String(30), unique=True, nullable=False)
    password = Column(String(80), nullable=False, default="")
    description = Column(String(30), unique=False, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True, server_default=db_true())
    is_admin = Column(Boolean, nullable=False, default=False, server_default=db_false())

    def __str__(self):
        return self.id
    def get_id(self):
        return self.id
    def get(id):
        return User.query.filter_by(id=id).first()
