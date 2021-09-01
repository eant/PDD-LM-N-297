import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'
respuesta = requests.get(url)

print("Código de respuesta:", respuesta.status_code)
print("URL de la petición:", respuesta.url)
#print("Contenido de la respuesta:", respuesta.content)
print("Contenido como texto:", respuesta.text)
print("Codificación:", respuesta.encoding)
respuesta.encoding = 'utf-8'
print("Contenido como texto:", respuesta.text)