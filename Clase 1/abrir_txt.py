archivo = open('fuentes/frutas.txt', 'r', encoding = 'utf-8')

for linea in archivo:
   #linea = linea.strip('\n')
   #linea = linea.replace('\n', '')
   linea = linea[:-1]
   print(linea)
   
archivo.close()