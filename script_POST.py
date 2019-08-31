import requests
import json 
Personas = {
    "nombre": "Anthony",
    "apellido": "Sanoja"
}

url = "http://httpbin.org/post"
response = requests.post(url, data=json.dumps(Personas))

print(response.content)

