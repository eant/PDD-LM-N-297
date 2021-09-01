import requests
import json
from pprint import pprint

with open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves.txt') as claves: keys = [clave.strip('\n') for clave in claves]

key = keys[0]

ciudad = "San Juan, Argentina"

url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&units=metric&lang=es&appid=" + key

objeto = json.loads(requests.get(url).text)

print("Descripción del clima:", objeto['weather'][0]['description'])
print("Temperatura: ", objeto['main']['temp'], "° C")

