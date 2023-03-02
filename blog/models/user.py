from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from blog.models.databases import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(255))
    email = Column(String(255), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
