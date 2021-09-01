import csv

with open('C:/Users\gonza\Desktop\PDD L-M\Clase 2\hospitales.csv', encoding = 'utf-8') as archivo_in, open('hospitales_out.csv', 'w',encoding = 'utf-8', newline='') as archivo_out:
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out)
    next(entrada)
    salida.writerow(['latitude','longitude','name','label'])
    for linea in entrada:
        coordenadas = linea[0][7:-1].split()
        direccion = ' '.join([linea[5],linea[6]])
        salida.writerow([coordenadas[1],coordenadas[0],direccion,linea[3]])
        