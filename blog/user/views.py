from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint(
    'user',
    __name__,
    static_folder='../static',
    url_prefix='/users'
)

USERS = {
    1: 'Alice',
    2: 'Mike',
    3: 'Tyler'
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
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'User ID {pk} not found')
    return render_template(
        'users/details.html',
        user_name=user_name,
    )
