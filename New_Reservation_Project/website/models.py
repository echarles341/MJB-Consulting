from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(3000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'))


class User(db.Model, UserMixin):
    id = db.column(db.Integer, primary_key=True)
    email = db.column(db.String(150), unique=True)
    password = db.column(db.String(100))
    first_name = db.column(db.String(50))
    last_name = db.column(db.String(100))
    notes = db.relationship('Note')
