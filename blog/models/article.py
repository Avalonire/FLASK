from sqlalchemy import Column, Integer, String, Boolean
from blog.models.databases import db


class Article(db.Model):
    __tablename__ = 'articles'

    title = Column(String(255))
    text = Column(String)

