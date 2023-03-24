from flask_combo_jsonapi import ResourceList

from blog.models.author import Author
from blog.models.databases import db
from blog.schemas import AuthorSchema


class AuthorBase(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorList(AuthorBase):
    pass


class AuthorDetail(AuthorBase):
    pass
