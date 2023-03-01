from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound
from mimesis import Person

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


