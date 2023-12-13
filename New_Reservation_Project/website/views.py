from flask import Blueprint, render_template
#define this file as a blueprint which contain the URL

views = Blueprint('views', __name__)

@views.route('/')
def home():
#    return "test 123"
    return render_template("home.html")
# "<h1>Test</h1>"