import requests
import json
import pprint

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)
#pprint.pprint(objeto)

for i in range(len(objeto['features'])):
   nombre = objeto['features'][i]['properties']['NOMBRE']
   domicilio = objeto['features'][i]['properties']['DOM_NORMA']
   print(nombre, '-', domicilio)
