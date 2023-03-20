from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from rest_framework.exceptions import NotFound
from sqlalchemy.orm import joinedload

from blog.forms.article import CreateArticleForm
from blog.models.article import Article, Tag
from blog.models.author import Author
from blog.models.databases import db

article = Blueprint('article', __name__, url_prefix='/article', static_folder='../static')


@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )


@article.route('/<int:article_id>', methods=['GET'])
def article_detail(article_id):
    _article: Article = Article.query.filter_by(
        id=article_id
    ).options(
        joinedload(Article.tags)
    ).one_or_none()

    if not _article:
        raise NotFound
    return render_template(
        'articles/details.html',
        article=_article,
    )


@article.route('/create/', method={'GET'})
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    return render_template(
        'articles/create.html',
        form=form
    )


@article.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if current_user.author:
            _article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author = current_user.author

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.article_details', article_id=_article.id))

    return render_template(
        'articles/create.html',
        form=form
    )
