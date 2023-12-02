from flask import Flask


# define the app
# initialize app
# create secret key to secure (encrypt)website cookies
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2023 python demo project 5097'

    # register the blueprint (it indicates where the file is been imported from)
    from .views import views
    from .auth import auth
    # register the blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # to run the app the return app
    return app
