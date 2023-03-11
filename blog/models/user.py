from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from blog.models.databases import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(80), unique=True, nullable=False)
    password = db.Column(String(255))
    email = db.Column(String(255), unique=True)
    is_staff = db.Column(Boolean, nullable=False, default=False)

    def __init__(self, email, username, password):
        self.email = email
        self.password = password
        self.username = username
