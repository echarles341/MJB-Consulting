from flask import Flask, request, jsonify
app = Flask(__name__)

import http.client

conn = http.client.HTTPSConnection("real-time-finance-data.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "dcc31d2418mshb50296504b9cb72p184808jsn9e45d344d8de",
    'X-RapidAPI-Host': "real-time-finance-data.p.rapidapi.com"
}

conn.request("GET", "/search?query=Apple&language=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

app = Flask(__name__)

@app.route("/")

def home():
    return "Home"

if __name__=="__main__":
    app.run(debug=true)