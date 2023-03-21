import click

from blog.models.databases import db


@click.command('creat-init-tags')
def create_init_tags():
    from blog.models.article import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gh', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {",".join(tags)}')
