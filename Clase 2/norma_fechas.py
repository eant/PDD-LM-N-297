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

fecha = '13/2/2019'
normalizadorFechas(fecha, '%d/%m/%Y')

fecha = "2/13/2019"
normalizadorFechas(fecha, '%m/%d/%Y')

fecha = "02/19" #(mes/año)
normalizadorFechas(fecha, '%m/%y', '%m-%Y')

fecha = '20191302'
normalizadorFechas(fecha, '%Y%d%m')

fecha = "2019-13-02 14:23:33"
normalizadorFechas(fecha, '%Y-%d-%m %H:%M:%S')

fecha = "13/February/2019"
normalizadorFechas(fecha, '%d/%B/%Y')

fecha = "13 days after February 2019"
normalizadorFechas(fecha, '%d days after %B %Y')

fecha = '13/Enero/2019'
normalizadorFechas(traductorFecha(fecha), '%d%m%Y')