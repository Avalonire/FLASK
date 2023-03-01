from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("Database tables created!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(username="admin", is_staff=True, email='asd@123.com', password='123')
    james = User(username="james", email='134sf@123.com', password='222')
    db.session.add(admin)
    db.session.add(james)
