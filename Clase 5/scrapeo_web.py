from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.cuspide.com/cienmasvendidos'
respuesta  = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html,  features = 'html.parser')

libros = dom.find_all('article')

#for libro in libros: print(libro.figure.div.a['title'])
for i in range(len(libros)): print(i+1, libros[i].figure.div.a['title'])