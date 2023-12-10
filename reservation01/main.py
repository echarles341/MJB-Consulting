from flask import Flask
from views import views

app = Flask(__name__)

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
#@app.route('/')
#def index():
#    return '<h1>Please make your reservation!</h1>'

if __name__ == "__main__":
    app.run(debug=True, port=8000)
