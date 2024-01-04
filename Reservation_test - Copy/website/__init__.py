from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from os import path
from flask_login import LoginManager, current_user
#from models import User
import mysql.connector
from datetime import datetime


#app = Flask(__name__)

#sqlite3.connect
db = mysql.connector.connect(host='localhost',
                                     port=3306,
                                     user='admin',
                           database='reservation_appointment')

mycursor = db.cursor()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2023 python demo project 5097'
    #Add database to the project
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///reservation_appointment.db'
    #initialize the Database
    db.init_app(app)
    # db = SQLAlchemy(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    # Run the app
    # create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader()
    def load_user(id):
        return User.query.get(int(id))

    return app










 
   



