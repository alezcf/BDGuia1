import pymongo

def conectar_bd():
    cliente = pymongo.MongoClient("localhost", 27017)
    return cliente["test"], cliente

def mostrar_menu(): 
    print("Menú:")
    print("1. Listar todos los documentos")
    print("2. Crear un nuevo documento")
    print("3. Actualizar un documento")
    print("4. Eliminar un documento")
    print("5. Salir")

def listar_documentos(coleccion):
    print("Documentos en la colección:")
    for documento in coleccion.find():
        print(documento)

def crear_documento(coleccion):
    nombre = input("Ingrese el nombre del restaurante: ")
    building = input("Ingrese el número de edificio: ")
    street = input("Ingrese el nombre de la calle: ")
    zipcode = input("Ingrese el código postal: ")
    borough = input("Ingrese el distrito: ")
    cuisine = input("Ingrese el tipo de cocina: ")

    coord_lon = float(input("Ingrese la longitud de coordenada: "))
    coord_lat = float(input("Ingrese la latitud de coordenada: "))
    coordenadas = [coord_lon, coord_lat]

    nuevo_documento = {
        "name": nombre,
        "address": {
            "building": building,
            "street": street,
            "zipcode": zipcode,
            "coord": coordenadas
        },
        "borough": borough,
        "cuisine": cuisine,
        "grades": []
    }
    coleccion.insert_one(nuevo_documento)
    print("Documento creado exitosamente.")

def actualizar_documento(coleccion):
    nombre = input("Ingrese el nombre del restaurante a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco si no desea actualizar): ")
    nuevo_building = input("Ingrese el nuevo número de edificio (deje en blanco si no desea actualizar): ")
    nueva_calle = input("Ingrese el nuevo nombre de la calle (deje en blanco si no desea actualizar): ")
    nuevo_zipcode = input("Ingrese el nuevo código postal (deje en blanco si no desea actualizar): ")
    nuevo_distrito = input("Ingrese el nuevo distrito (deje en blanco si no desea actualizar): ")
    nuevo_tipo_cocina = input("Ingrese el nuevo tipo de cocina (deje en blanco si no desea actualizar): ")
    nueva_lon = input("Ingrese la nueva longitud de coordenada (deje en blanco si no desea actualizar): ")
    nueva_lat = input("Ingrese la nueva latitud de coordenada (deje en blanco si no desea actualizar): ")

    update_query = {}
    if nuevo_nombre:
        update_query["name"] = nuevo_nombre
    if nuevo_building:
        update_query["address.building"] = nuevo_building
    if nueva_calle:
        update_query["address.street"] = nueva_calle
    if nuevo_zipcode:
        update_query["address.zipcode"] = nuevo_zipcode
    if nuevo_distrito:
        update_query["borough"] = nuevo_distrito
    if nuevo_tipo_cocina:
        update_query["cuisine"] = nuevo_tipo_cocina
    if nueva_lon and nueva_lat:
        update_query["address.coord"] = [float(nueva_lon), float(nueva_lat)]

    if update_query:
        coleccion.update_one({"name": nombre}, {"$set": update_query})
        print("Documento actualizado exitosamente.")
    else:
        print("No se especificaron campos para actualizar.")

def eliminar_documento(coleccion):
    nombre = input("Ingrese el nombre del restaurante a eliminar: ")
    resultado = coleccion.delete_one({"name": nombre})
    if resultado.deleted_count > 0:
        print("Documento eliminado exitosamente.")
    else:
        print("No se encontró ningún documento con el nombre proporcionado.")

def main():
    base_de_datos, cliente = conectar_bd()
    coleccion = base_de_datos["restaurants"]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_documentos(coleccion)
        elif opcion == "2":
            crear_documento(coleccion)
        elif opcion == "3":
            actualizar_documento(coleccion)
        elif opcion == "4":
            eliminar_documento(coleccion)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    # Cerrar la conexión al salir del programa
    cliente.close()
    print("¡Hasta luego!")

if __name__ == "__main__":
    main()
