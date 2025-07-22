# app/auth/models.py

from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # One-to-Many: One user → Many reports
    reports = db.relationship('Report', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"
