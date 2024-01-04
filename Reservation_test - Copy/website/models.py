from . import db
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.column(db.Integer, primary_key=True)
    email = db.column(db.String(120), unique=True, nullable=False)
    password = db.column(db.String(20), nullable=False)
    first_name = db.column(db.String(50))
    last_name = db.column(db.String(50))
    notes = db.relationship('Note', backref='author', lazy=True)
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'), nullable=False)
