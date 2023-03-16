from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models.article import Article

article = Blueprint('article', __name__, url_prefix='/article', static_folder='../static')


@article.route('/')
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )

# @article.route('/<int:pk>')
# def get_article(pk: int):
#     try:
#         article_info = Article
#     except KeyError:
#         raise NotFound(f'Article ID {pk} not found')
#     return render_template(
#         'articles/details.html',
#         article_info=article_info,
#     )
