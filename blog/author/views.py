from flask import Blueprint, render_template

from blog.models.author import Author

author = Blueprint(
    'author',
    __name__,
    static_folder='../static',
    url_prefix='/author'
)


@author.route('/')
def author_list():
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
    )
