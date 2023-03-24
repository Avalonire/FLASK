from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api
from flask_migrate import Migrate
from flask_admin import Admin

from blog.admin.views import CustomAdminIndexView


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            'Tags': 'Tags API',
            'User': 'User API',
            'Author': 'Author API',
            'Article': 'Article API',
        }
    )
    return api_spec_plugin


migrate = Migrate()
admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)
