from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\chromedriver.exe', options = options)

#driver.execute_script('alert("Hola Mundo")')
driver.get('https://www.lanacion.com.ar/')

sleep(3)

script_scroll_js = """
   let fin_pantalla = document.body.scrollHeight
   window.scrollTo(0, fin_pantalla)
   return fin_pantalla
   
"""
pos_actual = 0
pos_siguiente = driver.execute_script(script_scroll_js)
sleep(3)

while pos_actual != pos_siguiente:
   pos_actual = pos_siguiente
   pos_siguiente = driver.execute_script(script_scroll_js)
   sleep(3)
   print(pos_actual)
   
print("Llegamos al final de la página")

html = driver.execute_script("return document.documentElement.outerHTML")

driver.quit()

dom = BS(html, 'html.parser')
titulares = dom.find_all(class_="com-title --xs")
for titular in titulares:
   titulo = titular.a.text
   link  = titular.a['href']
   print(titulo, link)
   print()