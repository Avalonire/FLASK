from flask import Blueprint, redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from blog.admin.routes import admin

admin_bp = Blueprint('admin', __name__)


class CustomAdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class CustomAdminIndexView(AdminIndexView):

    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth.login'))
        return super().index()


class TagAdminView(ModelView):
    column_searchable_list = ('name',)
    create_modal = True
    edit_modal = True


class ArticleAdminView(ModelView):
    can_export = True
    export_types = ('csv', 'xlsx')
    column_filters = ('author_id',)


class UserAdminView(ModelView):
    column_exclude_list = ('password',)
    column_details_exclude_list = ('password',)
    column_export_exclude_list = ('password',)
    can_view_details = False
    can_delete = False
    can_edit = False
    can_create = False
    column_editable_list = ('first_name', 'last_name')
