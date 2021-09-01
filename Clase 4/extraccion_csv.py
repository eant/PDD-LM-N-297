import requests

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)

contenido = respuesta.text
with open('peliculas.csv', 'w') as archivo:
   archivo.write(contenido)