import requests

r = requests.get("http://httpbin.org/post")
json= r.json()