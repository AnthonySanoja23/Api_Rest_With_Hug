import requests

r = requests.get("https://xkcd.com/info.0.json")
json= r.json()
print(json)