import requests
import json 
Personas = {
    "nombre": "Jose",
    "apellido": "Sanoja",
    "Edad":"25"
}

url = "http://localhost:8000"
response = requests.post(url, data=json.dumps(Personas))

print(response.json())

