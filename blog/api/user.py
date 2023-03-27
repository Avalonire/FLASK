from flask_combo_jsonapi import ResourceList

from blog.api.permissions.user import UserPermission
from blog.models import User
from blog.models.databases import db
from blog.schemas import UserSchema


class UserBase(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }


class UserList(UserBase):
    data_layer = {
        'permission_get': [UserPermission],
    }


class UserDetail(UserBase):
    data_layer = {
        'permission_patch': [UserPermission],
    }
