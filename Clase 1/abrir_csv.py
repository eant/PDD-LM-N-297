archivo = open('subtes.csv', encoding = 'utf-8')
for linea in archivo:
   linea = linea.strip('\n')
   lista = linea.split(',')
   print(lista[2])
   
archivo.close()