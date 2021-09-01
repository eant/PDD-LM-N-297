from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

estudiante = {'nombre': 'Ana', 'apellido': 'Falda', 'dni': 39521368}

cliente.universidad.alumnos.insert_one(estudiante)

bd = cliente['universidad']
coleccion = bd['alumnos']

estudiantes = [{'nombre': 'Pablo', 'apellido': 'Jiménez', 'dni': 29452132},
               {'nombre': 'Gabriela', 'apellido': 'Perez'},
               {'nombre': 'Pedro', 'apellido': 'Ramone', 'dni': 25145963, 'hijos':[{'nombre': 'Juan', 'edad': 12}, {'nombre': 'Jimena', 'edad': 10}]}
               ]

coleccion.insert_many(estudiantes)
print("Datos subidos")