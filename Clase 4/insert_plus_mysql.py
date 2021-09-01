import mysql.connector

with open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves_mysql.txt') as claves:
   #claves_mysql = [clave for clave in claves]
   claves_mysql = []
   for clave in claves:
      claves_mysql.append(clave)

conexion = mysql.connector.connect(host = claves_mysql[0],
                                   database = claves_mysql[1],
                                   user = claves_mysql[2],
                                   password = claves_mysql[3])

cursor = conexion.cursor()
cursor.execute("SELECT dni FROM alumnos")
lista_dnis = [dni[0] for dni in cursor]
# lista_dnis = []
# for dni in cursor:
#    lista_dnis.append(dni[0])
   
while True:
    vDni = input("Ingrese el dni (Enter para salir): ")
    if vDni =='': break
    elif int(vDni) in lista_dnis: print("Este alumno ya fue ingresado")
    else:
       vNombre = input("Ingrese el nombre: ")
       vApellido = input("Ingrese el apellido:")
       vEmail = input("Ingrese el email:")
       vFecha_nac = input("Ingrese la fecha de nacimiento (AAAA-MM-DD):")
       query = 'INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES (%s,%s,%s,%s,%s)'
       cursor.execute(query, (vNombre, vApellido, vDni, vEmail,vFecha_nac ))
       print("Datos cargados")

conexion.commit()
print("Datos subidos")
cursor.close()
conexion.close()