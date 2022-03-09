# Laboratorio #2
#  Instalación y uso de una base de datos key-value en clúster: Caso REDIS

En este Folder se encuentra el codigo de la realizacion del Laboratorio #2. ademas se indican los requisitos para su correcto funcionamiento
y los comandos para la correcta ejecucion de este. 

## Requisitos

Los requisitos para este Laboratorio son los siguientes:

- Python 3.9.6
- Docker 20.10.12
- Redis 6.2.6

## Ejecucion

Para la correcta ejecucion de este codigo se debe de realizar de la siguiente manera: 

Primero que todo se debe de ejecurtar el **Docker-compose.yml** de la siguiente manera 
```
$ docker-compose up 
```
 
Despues de ejecutar este archivo hay dos maneras de realizar las operaciones en Redis una es a traves de redis-cli dentro del contenedor de Docker
y la segunda es ejecutando el archivo de python adjunto.

**Para realizar las operaciones a traves de redis-cli en una nueva terminal se ejecuntan los siguientes comandos**

```
$ docker ps  //Con este comando se mostraran la informacion de los contenedores
$ docker exec -it [CONTAINER ID] bash // de esta manera se ingresa al contenedor donde se encuentra la imagen de Redis
$ redis-cli -a [password] // Despues de ingresado este comando se podran realizar las operaciones CRUD
```

**Para realizar las operaciones a traves del archivo de python se realizan los siguiente comandos**
En una terminal nueva ser ejecuta 
```
$ redis-server
```
ahora en otra terminal se ejecuta el archivo python de la siguiente manera 

```
Python redis-operations.py [Host]
```

