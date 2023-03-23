
from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
from blog.models import article, user
from blog.extensions import admin
from blog.models.databases import db

admin.add.view(TagAdminView(article.Tag, db.session, category='Models'))
admin.add.view(ArticleAdminView(article, db.session, category='Models'))
admin.add.view(UserAdminView(user, db.session, category='Models'))
