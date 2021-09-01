import csv

with open('C:/Users\gonza\Desktop\PDD L-M\Clase 1\peliculas.csv', encoding='utf-8') as archivo_in, open('peliculas_out2.csv', 'w', encoding = 'utf-8', newline = '') as archivo_out:
   entrada = csv.reader(archivo_in)
   salida = csv.writer(archivo_out, delimiter = ';')
   salida.writerow(['título', 'director', 'año'])
   for linea in entrada: salida.writerow([linea[0], linea[2], linea[1]])
