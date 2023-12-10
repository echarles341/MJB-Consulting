from flask import Blueprint, render_template, request, jsonify
from pip._internal.commands import index

views = Blueprint(__name__, "views")


# create flask application and initialize flask
# app = Flask(__name__)

# create a route and define the route
@views.route('/')
def home():
    return render_template(index.html, name="Michael")

@views.route('/profile/<email>')
def profile(email):
    args = request.args
    name = args.get('name')
    return render_template(index.html, name="email")

@views.route('/profile/<email>')
def profile(email):
#    args = request.args
#    name = args.get('email')
    return render_template('profile.html')

#(index.html, name="email")


@views.route('/json')
def get_json(email):
    return jsonify({'name, address, email'})

#to request incoming data from user
@views.route('data')
def get_data():
    data = request.json
    return jsonify(data)