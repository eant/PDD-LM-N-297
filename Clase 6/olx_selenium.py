from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\chromedriver.exe', options = options)

#driver.execute_script('alert("Hola Mundo")')
driver.get('https://www.olx.com.ar/items/q-Motorola-g9')

sleep(3)

script_js = """
   let boton = document.querySelector('[data-aut-id="btnLoadMore"]')
   if (boton){
         boton.click()
      }
   else {
         return "No existe"
      }
"""
while driver.execute_script(script_js) != "No existe": sleep(3)

sleep(2)
html = driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

dom = BS(html, 'html.parser')
productos = dom.find_all(class_="IKo3_")
for producto in productos:
   precio = producto.find(class_="_89yzn").string
   descripcion = producto.find(class_="_2tW1I").string
   print(descripcion + ': ' + precio)
   