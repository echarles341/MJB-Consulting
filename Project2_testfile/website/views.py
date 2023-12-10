from flask import Flask
#create flask application and initialize flask
app = Flask(__name__)

#create a route and define the route
@app.route('/')
def home():
    return "Please make your reservation "

if __name__=='__main__':
    app.run(debug=True)





