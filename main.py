import pymongo

cliente = pymongo.MongoClient("localhost", 27017)
base_de_datos = cliente["test"]
coleccion = base_de_datos["restaurants"]

# Leer todos los documentos en la colección
documentos = coleccion.find()

# Imprimir los documentos
for documento in documentos:
    print(documento)
