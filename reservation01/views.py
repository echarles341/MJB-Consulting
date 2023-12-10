from flask import Blueprint, render_template
#define this file as a blueprint which contain the URL

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "Please make your reservation"

