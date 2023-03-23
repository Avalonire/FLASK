from flask_combo_jsonapi import ResourceList

from blog.models.databases import db
from blog.models.article import Tag
from blog.schemas import TagSchema


class TagBase(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagList(TagBase):
    pass


class TagDetail(TagBase):
    pass
