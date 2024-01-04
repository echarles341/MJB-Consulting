from flask import Flask
# from . import db
# set up database
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# define the app
# initialize app
# create secret key to secure (encrypt)website cookies
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2023 python demo project 5097'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    #    register the blueprint (it indicates where the file is being imported from)
    #    from .views import views
    #    from .auth import auth
    #    register the blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # create database

   from .models import User, Note


    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader()
    def load_user(id):
        return User.query.get(int(id))

    return app


#    to run the app the return app
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


