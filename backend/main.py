from app import create_app, db
from app.models import User
from config import Config

app = create_app(Config)

@app.before_first_request
def create_db():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()
    #admin = User('admin', 'admin@example.com')
    #db.session.add(admin)
    #guests = [User('guest1', 'guest1@example.com'),
              #User('guest2', 'guest2@example.com'),
              #User('guest3', 'guest3@example.com'),
              #User('guest4', 'guest4@example.com')]
    #db.session.add_all(guests)
    #db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
