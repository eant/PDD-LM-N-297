from bs4 import BeautifulSoup as BS
import requests
import csv

url = 'https://www.ambito.com/'
respuesta  = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html,  features = 'html.parser')

tabla = [['N°', 'Título', 'Link']]

titulares = dom.find_all(class_='title')

contador = 1
for titular in titulares:
   titulo = titular.text
   link = titular.a['href']
   #print(contador, titulo, link)
   contador += 1
   fila = [contador, titulo, link]
   tabla.append(fila)
   
with open('noticias.csv', 'w', newline='') as file:
   salida = csv.writer(file)
   salida.writerows(tabla)