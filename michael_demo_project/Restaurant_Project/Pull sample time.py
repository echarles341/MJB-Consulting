import requests

r = requests.get('https://httpbin.org/basic-auth/Michael/testing123', auth=('Michael','testing123'))
print(r)


