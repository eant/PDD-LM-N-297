import requests
import json
from pprint import pprint
import csv

with open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves.txt') as claves: keys = [clave.strip('\n') for clave in claves]

key = keys[0]

log_error = open('log_error_sol_360.txt', 'w')
archivo = open('sucursales_sol_360.csv')
archivo_csv = csv.reader(archivo, delimiter = ';')
ciudades = [linea[0] for linea in archivo_csv]

for ciudad in ciudades:
   url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + ",Argentina&units=metric&lang=es&appid=" + key
   objeto = json.loads(requests.get(url).text)
   if objeto.get('weather') == None: log_error.write(ciudad + " - no encontrada\n")
   else:
      print("Ciudad: ", ciudad)
      print("Descripción del clima:", objeto['weather'][0]['description'])
      print("Temperatura: ", objeto['main']['temp'], "° C")

log_error.close()