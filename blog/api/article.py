from combojsonapi.event.resource import EventsResource
from flask import requests
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


class ArticleListEvent(EventsResource):

    def event_get_count(self):
        return {'count': Article.query.count()}

    def event_get_api_server(self):
        return {'count': requests.get('https://ifconfig.io/ip').text}


class ArticleDetailEvent(EventsResource):

    def event_get_count_by_author(self, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ArticleBase):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ArticleBase):
    pass
