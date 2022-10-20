from app import db
from app import app
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(length=100), nullable=False)
    blogs = db.relationship('Post')

    def __int__(self, username, password):
        self.username = username
        self.password = password


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=100), db.ForeignKey(User.username), nullable=True)
    created = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __init__(self, username, title, body):
        self.username = username
        self.title = title
        self.body = body
        self.created = datetime.now()

    def update_post(self, title, body):
        self.title = title
        self.body = body
        db.session.commit()


def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
