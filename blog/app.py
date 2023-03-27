from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from flask import Flask, render_template
from flask_combo_jsonapi import Api

from blog.admin.views import admin_bp
from blog.auth.views import auth, login_manager
from blog.extensions import migrate, admin
from blog.report.views import report
from blog.user.views import user
from blog.article.views import article
from blog.models.databases import db


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hq0wt)+6vb18zmf=q%9ad&!=(7k24c&*io)^v6@$#u_*i#(%qb'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from .models import User

    @app.route("/")
    def index():
        return render_template("index.html")

    migrate.init_app(app, db)
    login_manager.init_app(app)

    db.init_app(app)
    register_blueprints(app)
    admin.init_app(app)
    register_api(app)
    return app


def register_api(app: Flask):
    from blog.api.tag import TagList
    from blog.api.tag import TagDetail
    from blog.api.user import UserList
    from blog.api.user import UserDetail
    from blog.api.author import AuthorList
    from blog.api.author import AuthorDetail
    from blog.api.article import ArticleList
    from blog.api.article import ArticleDetail
    from blog.extensions import create_api_spec_plugin

    api = Api(
        app=app,
        plugins=[
            create_api_spec_plugin(app)
        ]
    )
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
    ]
    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(admin_bp)
