from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from os import path
from flask_login import LoginManager, current_user
#from models import User
import _sqlite3
from datetime import datetime


# class person:
# create a class person:
# def __init__(self, id_number= -1, first_name = -1, last_name= -1):
# self.id_number = id_number
# self.first_name = first_name
# self.last_name = last_name
# connect = _sqlite3.connect('database.db')
# cursor which allow the interface to be connected to the database
# self.cursor = self.connection.cursor()
    
# load_person(self, id_number):
# self.cursor.execute("""" SELECT * FROM persons WHERE id = {}"""").format(id_number))
    
# results = cursor.fetchone()
    
# Result
# results = self.cursor.fetchone()
# self.id_number = id_number
# self.first_name = results[1]
# self.last_name = results[2]


# object
# p1 = person()
# p1.load_person(1)
# print(p1.first_name)
# print(p1.last_name)
# print(p1.id_number)

# enter new data into the database as a row entry

# def insert_person(self):
# self.cursor.execute("""" INSERT INTO persons VALUES ({}, '{}', '{}')"""".format(self.id_number, self.first_name, self.last_name))

# sefl.connection.commit()

# self.connection.close()

# p1 = person(7, "Alex","Brown")
# p1.instert_person()

# connect = _sqlite3.connect('database.db')
# cursor which allow the interface to be connected to the database
# self.cursor = connection.cursor()

# select.excute("SELECT * FROM persons")
# results = cursor.fetchall()
# print (results)

# connection.close()






#Final step: combine object oriented database with object oriented programming
# create a class person:
# def __init__(self, id_number, first_name, last_name):
# self.id_number = id_number
# self.first_name = first_name
# self.last_name = last_name
# connect = _sqlite3.connect('database.db')
# cursor which allow the interface to be connected to the database
# self.cursor = connection.cursor()

# load a person from the table and converts it into a python object.

# def load_database(self, id_number):

# execute self curson
# cursor.execute(""" SELECT * FROM database  WHERE id = ()""").format(id_number)

# Result
# results = cursor.fetchone()
# self.id_number = id_number
# self.first_name = results[1]
# self.last_name = results[2


# 1 create new table in models.py
# 2 Method to execute a query
# cursor.execute(""" CREATE TABLE if not EXISTS database (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)""")
# To enter data in the table
# cursor.execute("""" INSERT INTO database VALUES('Paul','Smith'), ('John', 'Doe')"""")
# To print a group of the same last name
# cursor.execute("""SELECT * FROM database WHERE last_name = 'Smith' """")
# roows = cursor.fetchall()
# print(rows)
# connection.commit()
#connection.close()

# app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "datbase.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2023 python demo project 5097'
    #Add database to the project
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB_NAME.db'
    #initialize the Database
    db.init_app(app)
    # db = SQLAlchemy(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    # Run the app
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader()
    def load_user(id):
        return User.query.get(int(id))


    return app

# Create the database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('created Database')








 
   



