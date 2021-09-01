import requests
import csv
from io import StringIO

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)

contenido = respuesta.text

file = StringIO(contenido)

objeto_csv = csv.reader(file)

with open('peliculas.csv', 'w', newline='') as archivo:
   for linea in objeto_csv:
      archivo.write(linea[0] + ',' + linea[1] + '\n')