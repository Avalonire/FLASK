from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from mimesis import Text

from blog.user.views import USERS

article = Blueprint(
    'article',
    __name__,
    static_folder='../static',
    url_prefix='/articles'
)

ARTICLES = {
    1: {'title': Text().title(),
        'author': USERS[2]['fullname'],
        'text': Text().text(10),
        },

    2: {'title': Text().title(),
        'author': USERS[1]['fullname'],
        'text': Text().text(9),
        },
    3: {'title': Text().title(),
        'author': USERS[3]['fullname'],
        'text': Text().text(16),
        },
    4: {'title': Text().title(),
        'author': USERS[5]['fullname'],
        'text': Text().text(7),
        },
    5: {'title': Text().title(),
        'author': USERS[4]['fullname'],
        'text': Text().text(15),
        },
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_info = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Article ID {pk} not found')
    return render_template(
        'articles/details.html',
        article_info=article_info,
    )
