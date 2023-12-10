from flask import Flask
from views import views

#create flask application and initialize flask
app = Flask(__name__)

#create a route and define the route
app.register_blueprint(views, url_prefix="/")

if __name__=='__main__':
    app.run(debug=True)
