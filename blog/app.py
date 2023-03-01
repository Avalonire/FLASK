from flask import Flask, render_template

from blog.auth.views import auth, login_manager
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

    login_manager.init_app(app)

    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
