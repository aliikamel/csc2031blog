from app import db


class User(db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(length=100), nullable=False)

    def __int__(self, username, password):
        self.username = username
        self.password = password