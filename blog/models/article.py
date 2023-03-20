from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from blog.models.databases import db

article_tag_associations_table = Table(
    'article_tag_associations',
    db.metadata,
    db.Column('article_id', db.Integer, ForeignKey('article.id'), nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tag.id'), nullable=False),
)


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_associations_table, back_populates='articles')


class Tag(db.Model):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    articles = relationship('Article', secondary=article_tag_associations_table, back_populates='tags')
