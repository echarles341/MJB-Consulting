import requests
from htmldate import find_date

html = requests.get(
 'https://www.theguardian.com/world/2022/may/01/russia-trolling-ukraine-traction-tiktok').content.decode('utf-8')
date = find_date(html)
print(date)