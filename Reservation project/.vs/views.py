from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

#create flask application and initialize flask
# app = Flask(__name__)

#create a route and define the route
@views.route('/')
def home():
    return render_template("index.html")

