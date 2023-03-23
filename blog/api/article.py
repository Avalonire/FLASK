from flask_combo_jsonapi import ResourceList

from blog.models.databases import db
from blog.models.article import Article
from blog.schemas import ArticleSchema


class ArticleBase(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleList(ArticleBase):
    pass


class ArticleDetail(ArticleBase):
    pass
