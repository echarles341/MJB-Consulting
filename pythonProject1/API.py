import requests

URL ="hotels4.p.rapidapi.com"


response = requests.get(URL)

print(response.text)
