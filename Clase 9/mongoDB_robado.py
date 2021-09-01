from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={}
project={
    'nombre': 1, 
    'apellido': 1, 
    '_id': 0
}
sort=list({
    'apellido': 1
}.items())
skip=1
limit=2

result = client['universidad']['alumnos'].find(
  filter=filter,
  projection=project,
  sort=sort,
  skip=skip,
  limit=limit
)
for estudiante in result:
   print(estudiante)