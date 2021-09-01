from bs4 import BeautifulSoup as BS

archivo_html = open('web_ejemplo.html', encoding='utf-8')
dom = BS(archivo_html, features = 'html.parser')

#print(dom.prettify())

#primer_link = dom.a
# primer_link = dom.find('a')
#print(primer_link.string)

# todos_los_links = dom.find_all('a')
# for link in todos_los_links:
#    print(link.string)

# print(primer_link['class'])
# print(primer_link['href'])

#parrafo = dom.find(id='otros-integrantes')
#links = parrafo.find_all('a')

#parrafo_historia = dom.find_all('p', class_ = 'historia')
#parrafo_historia = dom.find_all('p', attrs = {'class': 'historia'})

#historia = dom.find(attrs = {'data-minumero':'124124'})

