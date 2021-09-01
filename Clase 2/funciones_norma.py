from datetime import datetime

def normalizadorFechas(fecha, patron_in, patron_out = '%d-%m-%Y'):
   objeto_fecha = datetime.strptime(fecha, patron_in)
   fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
   print(fecha, '->', objeto_fecha, '->', fecha_normalizada)

def traductorFecha(fecha):
   meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
   lista = fecha.split('/')
   mes = lista[1].upper()
   nro_mes = meses.index(mes) + 1
   fecha_aux = lista[0] + str(nro_mes) + lista[2]
   return fecha_aux