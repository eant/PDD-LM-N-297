from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

bd = cliente['universidad']
coleccion = bd['alumnos']

estudiantes = coleccion.find()

# for estudiante in estudiantes:
#    print(estudiante)

#estudiante_especial = coleccion.find({'dni': 39521368})
estudiante_especial = coleccion.find({'hijos.nombre': 'Jimena'})


for estudiante in estudiante_especial:
   print(estudiante)