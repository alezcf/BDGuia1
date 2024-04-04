# Manual de Uso - Guía 1


## ***Instalación de Mongo***

    sudo apt update
    sudo apt install mongodb


## ***Instalación libreria en virtualización de Python***

    pip install pymongo


## ***Importación de colecciones***

Inicialmente, se debe inicializar el proceso para importar una colección en `formato JSON` a nuestro programa Mongo, para ello, nos dirigiremos a la carpeta en donde está dicho archivo y se utilizará el siguiente comando:

    mongoimport --db test --collection restaurants --drop --file dataset.json

dicha operación hará que se guarde la colección `restaurants` en nuestro programa Mongo previamente instalado. 


## ***Inicio de Servicios***

Se tendrá que inicializar Mongo mediante terminal, lo cual se puede realizar con el comando mediante terminal 

    sudo service mongod start

El éxito de dicha operación se puede verificar mediante el `estatus actual` de la base de datos mediante

    sudo service mongod status

Es necesario inicializar el servicio de Mongo con el comando

    mongosh
    
Ahí podremos visualizar todas las colecciones importadas utilizando

    show collections
    
Únicamente debería ser visible una con el nombre de `restaurants`.

Para continuar, será necesario `iniciar la virtualización de Python3`

    python main.py

El cual mediante terminal, permitirá accionar distintas acciones mediante el CRUD desarrollado.


## ***Funcionalidades del programa***

El programa permite realizar las siguientes operaciones sobre la colección de restaurantes:

    1- Listar todos los documentos.
    2- Crear un nuevo documento.
    3- Actualizar un documento existente.
    4- Eliminar un documento existente.
    5- Salir del programa.

Finalmente, queda seleccionar la opción correspondiente según la operación que desees realizar mediante la terminal.


## ***Cierre del programa***

Para detener el servicio de MongoDB, puedes utilizar el comando

    sudo service mongod stop
