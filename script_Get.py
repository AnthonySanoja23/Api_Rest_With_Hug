import requests

r = requests.get("http://httpbin.org/get")
json= r.json()
print(type(json))
