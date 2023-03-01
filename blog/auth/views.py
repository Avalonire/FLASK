from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from blog.models import User

auth = Blueprint(
    'auth',
    __name__,
    static_folder='../static',
)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template(
            'auth/login.html',
        )


@auth.route('/logout')
def logout():
    return 13


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))


@auth.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="User name not passed!")

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"User {username!r} not found!")
    login_user(user)
    return redirect(url_for("index"))


@auth.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


__all__ = [
    "login_manager",
    "auth",
]
