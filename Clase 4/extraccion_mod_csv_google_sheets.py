import requests
import csv
from io import StringIO

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT651r_njGaU1HoLcQJKHKO3-eUftz7TxK5s4a4llLj73uwu6MKK5a3MdOI_xGCapJDrSFs9TiPEagN/pub?gid=34778314&single=true&output=csv'
respuesta = requests.get(url)

contenido = respuesta.text

file = StringIO(contenido)

objeto_csv = csv.reader(file)

with open('peliculas_google.csv', 'w', newline='') as archivo:
   for linea in objeto_csv:
      archivo.write(linea[0] + ',' + linea[1] + '\n')