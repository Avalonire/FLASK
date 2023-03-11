from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.exceptions import NotFound
from mimesis import Person
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash

from blog.forms.user import UserRegisterForm
from blog.models import User
from blog.models.databases import db

user = Blueprint(
    'user',
    __name__,
    static_folder='../static',
    url_prefix='/users'
)

human = Person()

USERS = {
    1: {
        'fullname': human.full_name(),
        'name': human.first_name(),
        'last_name': human.last_name(),
        'gender': human.gender(),
        'mail': human.email(),
    },
    2: {
        'fullname': human.full_name(),
        'name': human.first_name(),
        'last_name': human.last_name(),
        'gender': human.gender(),
        'mail': human.email(),
    },
    3: {
        'fullname': human.full_name(),
        'name': human.first_name(),
        'last_name': human.last_name(),
        'gender': human.gender(),
        'mail': human.email(),
    },
    4: {
        'fullname': human.full_name(),
        'name': human.first_name(),
        'last_name': human.last_name(),
        'gender': human.gender(),
        'mail': human.email(),
    },
    5: {
        'fullname': human.full_name(),
        'name': human.first_name(),
        'last_name': human.last_name(),
        'gender': human.gender(),
        'mail': human.email(),
    }
}


@user.route('register', method=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.details', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email not uniq!')
            return render_template('users/register.html', form=form)

    _user = User(
        email=form.email.data,
        username=form.username.data,
        password=generate_password_hash(form.password.data),
    )

    db.session.add(_user)
    db.session.commit()

    login_user(_user)

    return render_template(
        'users/register.html',
        form=form,
        errors=errors,
    )


@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f'User {pk} not found!')
    return render_template(
        'users/details.html',
        user_info=_user,
    )
