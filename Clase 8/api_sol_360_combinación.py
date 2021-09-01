import requests
import json
from pprint import pprint
import csv

with open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves.txt') as claves: keys = [clave.strip('\n') for clave in claves]

key_open_weather = keys[0]
key_open_geo = keys[1]

log_error = open('log_error_sol_360.txt', 'w')
archivo = open('sucursales_sol_360.csv')
archivo_csv = csv.reader(archivo, delimiter = ';')
ciudades = [linea[0] for linea in archivo_csv]

for ciudad in ciudades:
   #Acá accedo a la API de geolocalización
   url = 'https://api.opencagedata.com/geocode/v1/json?q=' + ciudad + '&key=' + key_open_geo + '&language=es&pretty=1'
   objeto = json.loads(requests.get(url).text)
   #pprint(objeto)
   lat = objeto['results'][0]['geometry']['lat']
   lon = objeto['results'][0]['geometry']['lng']
   
   #Acá accedo a la API del tiempo
   url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat)  + "&lon=" + str(lon) + "&units=metric&lang=es&appid=" + key_open_weather
   objeto = json.loads(requests.get(url).text)
   if objeto.get('weather') == None: log_error.write(ciudad + " - no encontrada\n")
   else:
      print("Ciudad: ", ciudad)
      print("Descripción del clima:", objeto['weather'][0]['description'])
      print("Temperatura: ", objeto['main']['temp'], "° C")
   
log_error.close()