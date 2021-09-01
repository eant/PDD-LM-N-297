import json
import pprint

with open('amo.json') as archivo:
   amo = json.load(archivo)

pprint.pprint(amo)