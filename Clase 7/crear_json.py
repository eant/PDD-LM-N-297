import pprint
import json

#Diccionario
perro = {'nombre': 'Rocco',
         'tipo': 'perro',
         'raza': 'labrador'}

gato = {'nombre': 'Felix',
         'tipo': 'gato',
         'raza': 'persa',
         'edad': 6}
#Variable
edad = 5

#Lista
le_gusta = ['Comer', 'Ladrar', 'Correr a las palomas']

#Combinación
perro.update({'edad': edad, 'le gusta': le_gusta})

#pprint.pprint(perro)

amo = {'nombre': 'Juan Carlos',
       'tipo': 'humano',
       'le gusta': ['Una buena conversación', 'Los fichines', 'Fútbol'],
       'edad': 38,
       'mascota': [perro, gato]}

pprint.pprint(amo)

with open('amo.json', 'w') as archivo_json:
   json.dump(amo, archivo_json, ensure_ascii=False, indent=3)