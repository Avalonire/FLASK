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
    return render_template(
        'users/list.html',
        user=USERS,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_info = USERS[pk]
    except KeyError:
        raise NotFound(f'User ID {pk} not found')
    return render_template(
        'users/details.html',
        user_info=user_info,
    )
