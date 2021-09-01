import requests
import json
import pprint

direccion = "Rivadavia 5200"
localidad = 'caba'

dir_codificada = requests.utils.quote(direccion + ', ' +  localidad)

#print(dir_codificada)

url = 'http://servicios.usig.buenosaires.gob.ar/normalizar/?geocodificar=True&direccion=' + dir_codificada

#print(url)

respuesta = requests.get(url).text
dir_normalizada = json.loads(respuesta)
#pprint.pprint(dir_normalizada)
print('latitud:',  dir_normalizada['direccionesNormalizadas'][0]['coordenadas']['y'])
print('longitud:',  dir_normalizada['direccionesNormalizadas'][0]['coordenadas']['x'])
