from flask import Blueprint, render_template

# define this file as a blueprint which contain the URL

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", text="Testing", user="Michael")


#        "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
