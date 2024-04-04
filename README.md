# Manual de Uso - Guía 1

Instalación de dependencias

Asegúrate de tener Python 3 y MongoDB instalados en tu sistema operativo. En sistemas basados en Linux, como Ubuntu, puedes instalar MongoDB utilizando el administrador de paquetes de tu distribución. En este caso que utilizamos Ubuntu, por lo tanto ejecutamos: 

sudo apt update
sudo apt install mongodb

Además, hay que tener instalado el paquete pymongo de Python, que es necesario para la comunicación con MongoDB "pip install pymongo".


Importación de colecciones 

Inicialmente, se debe inicializar el proceso para importar una colección en formato JSON a nuestro programa Mongo, para ello, nos dirigiremos a la carpeta en donde está dicho archivo y se utilizará el siguiente comando "mongoimport --db test --collection restaurants --drop --file dataset.json", dicha operación hará que se guarde la colección "restaurants" en nuestro programa Mongo previamente instalado. 


Inicio de Servicios

Se tendrá que inicializar Mongo mediante terminal, lo cual se puede realizar con el comando mediante terminal "sudo service mongod start". El éxito de dicha operación se puede verificar mediante el estatus actual de la base de datos mediante "sudo service mongod status". En caso de estar operativa, se puede pasar al siguiente paso.

Es necesario inicializar el servicio de Mongo bajo el comando "mongosh" en terminal. Una vez dentro del servicio, podremos visualizar todas las colecciones importadas bajo el comando "show collections", en este caso, únicamente debería ser visible una con el nombre de "restaurants". Este paso nos permite corroborar una correcta importación de las colecciones y datos de nuestro archivo JSON.

Para continuar, será necesario iniciar la virtualización de Python3 y desplazarse hacia la carpeta en donde está ubicado el código, una vez ahí, debe ser ejecutado mediante el comando "python main.py", el cual mediante terminal, permitirá accionar distintas acciones mediante el CRUD desarrollado.


Funcionalidades del programa

El programa permite realizar las siguientes operaciones sobre la colección de restaurantes:

    1- Listar todos los documentos.
    2- Crear un nuevo documento.
    3- Actualizar un documento existente.
    4- Eliminar un documento existente.
    5- Salir del programa.

Selecciona la opción correspondiente según la operación que desees realizar.


Cierre del programa

Una vez que hayas terminado de interactuar con la base de datos, puedes cerrar el programa y detener el servicio de MongoDB si así lo deseas. El programa también cerrará automáticamente la conexión con la base de datos al salir.

Para detener el servicio de MongoDB, puedes utilizar el comando "sudo service mongod stop".