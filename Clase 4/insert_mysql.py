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

nombre = 'Adalberto'
apellido = 'Carranza'
dni = '28456357'
email = "adalberto@nada.com"
fecha_nac = "1980-11-12"

# query = 'INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES("Adalberto", "Carranza", "28456357", "adalberto@nada.com", "1980-11-12")'

query = 'INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES(%s,%s,%s,%s,%s)'

cursor.execute(query, (nombre, apellido, dni, email, fecha_nac))

conexion.commit()
cursor.close()
conexion.close()
