import csv
archivo_in = open('peliculas.csv', encoding = 'utf-8')
tabla = csv.reader(archivo_in, delimiter = ',')
archivo_out = open('peliculas_salida.csv', 'w', encoding = 'utf-8')

archivo_out.write('título,director,año\n')

for linea in tabla:
   fila  = ','.join([linea[0], linea[2], linea[1]])
   archivo_out.write(fila + '\n')
   
archivo_in.close()
archivo_out.close()