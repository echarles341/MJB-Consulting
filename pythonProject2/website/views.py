#to render the template created
from flask import Blueprint, render_template, request
from pyexpat import model

# define this file as a blueprint which contain the URL

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


