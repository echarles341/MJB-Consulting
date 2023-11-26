import http.client

conn = http.client.HTTPSConnection("hotels4.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "dcc31d2418mshb50296504b9cb72p184808jsn9e45d344d8de",
    'X-RapidAPI-Host': "hotels4.p.rapidapi.com"
}

conn.request("GET", "/v2/get-meta-data", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))