# BDGuia1

Para inicializar el proceso, es necesario instalar la dependencia de Python3 y Mongo en el sistema operativo, en este caso se utilizó en un sistema linux, específicamente Ubuntu.

Inicialmente, se debe inicializar el proceso para importar una colección en formato JSON a nuestro programa Mongo, para ello, nos dirigiremos a la carpeta en donde está dicho archivo y se utilizará el siguiente comando "mongoimport --db test --collection restaurants --drop --file dataset.json", dicha operación hará que se guarde la colección "restaurants" en nuestro programa Mongo previamente instalado. 

Luego, se tendrá que inicializar Mongo mediante terminal, lo cual se puede realizar con el comando mediante terminal "sudo service mongod start". El éxito de dicha operación se puede verificar mediante el estatus actual de la base de datos mediante "sudo service mongod status". En caso de estar operativa, se puede pasar al siguiente paso.

Es necesario inicializar el servicio de Mongo bajo el comando "mongosh" en terminal. Una vez dentro del servicio, podremos visualizar todas las colecciones importadas bajo el comando "show collections", en este caso, únicamente debería ser visible una con el nombre de "restaurants". Este paso nos permite corroborar una correcta importación de las colecciones y datos de nuestro archivo JSON.
