
# Invera Todo Challenge

Este repositorio contiene la primera version del challenge de Invera (Python/Django Jr-SSr). Todos los detalles referentes a este defaío y sus requerimientos pueden ser encontrados [aquí](https://github.com/invera/todo-challenge?tab=readme-ov-file).

# Resumen del desarrollo realizado.
El objetivo principal de este desarrollo, es cumplir con los objetivos establecidos por el desafío. Por esta razón se desarrollo una pequeña aplicación, cuya estructura es muy simple, cuenta con 3 diferentes modelos (clases) que permiten a los usuarios agendar tareas para ser completadas.

Las clases son:

 - User
 - Task
 - Subtask

Los siguientes son los diagramas de Clases y E/R pensados para la aplicación:

![Diagram 1](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/Diagrama1.png)
![Diagram 2](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/Diagrama2.png)


# Como correr la aplicación.
Lo primero que se requiere es clonar el repositorio en la máquina local. Esto puede realizarse ejecutando el siguiente comando `git clone git@github.com:pereza94/todo-challenge.git` situandose dentro del directorio donde desea que el proyecto sea alojado.

Una vez hecho esto, es posible elegir entre 2 opciones para correr la aplicacion:
* Usando docker
* Creando su propio entorno virtual.

### Opcion A: Usando Docker
Una forma muy simple de probar el funcionamiento de la aplicación, es ejecutando la misma dentro de un Docker. Para esto es necesario contar con la aplicación `Docker Desktop` instalada en la computadora donde se buildeara el contenedor (en caso no de contar con la aplicación, la misma puede ser descargada desde [docker site](https://www.docker.com/products/docker-desktop/#).

Para verficar que la instalación fue exitosa, puede correr en su terminal el comando `command docker --version`. Si como resultado se muestra la version de Docker, el programa fue instalado exitosamente.
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_version.png?token=GHSAT0AAAAAACOYVBDTPXDGZCPSWUHIRJ7EZPHNKMQ)

Llegados a este punto, solo es necesario buildear el contenedor. Para esto asegurese que se encuentra en la carpeta correcta (debería ver las carpetas 'tasks', 'tests', ' todoChallenge' entre otras, y un archivo llamado `DockerFile`), y correr el siguiente comando `docker build -t todochallenge .`. Una vez finalizada la construcción del Docker, verá una imagen similar a la siguiente:

![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_build.png?token=GHSAT0AAAAAACOYVBDS3YBN4OURILOUBBCSZPHOJQA)

Seguidamente es necesario ejecutar el docker, con la siguiente instrucción:
` sudo docker run -it -p 9000:8000 todochallenge`
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_running.png?token=GHSAT0AAAAAACOYVBDSKMTOS5K6XBZXIDWOZPHOIWQ)
*Nota: en el ejemplo, la máquina local está escuchando en el puerto 9000, pero es posible elegir cualquier puerto que desee*

Finalmente, si todo salió bien, debería ver la documentación de swagger al visitar la URL:http://localhost:9000/swagger/docs/.

### Opción B: Instalando su propio entorno virtual

El primer paso es crear el entorno virtual, una forma simple de hacerlo es utilizando la herramienta `mkvirtualenv`. Esta herramienta esta disponible en  [here](https://virtualenvwrapper-docs-es.readthedocs.io/es/latest/install.html).

Para crear el entorno virtual es posible utilizar el siguiente comando:
`mkvirtualenv --python=python3.8 invera-challenge`

Una vez en la carpeta del repositorio, es necesario instalar las dependencias. Esto se puede realizar utilizando el siguiente comando:
`pip install -r requirements.txt`

Finalmente, es posible correr la aplicación ejecutando:
` python manage.py runserver` 
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/django-running-in-venv.png?token=GHSAT0AAAAAACOYVBDSQY4HOOUXBQ3IPWGKZPHPOCA)

*Nota: por defecto, django inicia el servidor escuchando en el puerto 8000. Pero es posible modificarlo pasando el puerot deseado como argumento, por ejemplo python manage.py runserver 0.0.0.0:8080`*

Si todo salió bien, debería ser posible chequear la documentación de swagger en http://localhost:8080/swagger/docs/.
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/swagger-documentation.png?token=GHSAT0AAAAAACOYVBDSNPE7XZADIFDNOJA2ZPHPRGA)


# Como interactuar con la aplicación
Una vez que la App esta corriendo, es posible interactuar con ella a través de requests. Actualmente existen diferentes herramientas que permiten realizar esto de una forma muy simple.

Por ejemplo, la aplicación provee swagger, en la ruta `/swagger/docs`. Esta pagina muestra todas las posible interacciones disponibles actualmente; y seteando las credenciales necesarias puede realizar tantas consultas como desee.

Existe un super usuario seteado en la aplicación, cuyo nombre de usuario y contraseña son: **challenge:ChallengePassword**
 ![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/swagger-image.png)

En la ruta `tasks/task` que permite listar todas las tareas almacenadas en la BD, están disponibles los siguites filtros:

 - ***description_contains***: retorna todas las tareas que en la descripción incluyan la palabra buscada.
 - ***name_contains***: retorna todas las tareas que en el nombre incluyan la palabra buscada
 - ***minimum_date***: retorna todas las tareas creadas luego de la fecha seleccionada. (El formato esperado para el ingreso de la fecha es dd-mm-yy)
 - ***maximum_date***: retorna todas las tareas creadas antes de la fecha seleccionada. (El formato esperado para el ingreso de la fecha es dd-mm-yy)

## Interactuar con la aplicación utilizando Postman

Otra opción para interactuar con la aplicación es utilizando postman. Para esto es posible utilizar [esta collection](https://github.com/pereza94/ImagesForReadmes/blob/draft/TodoChallenge.postman_collection.json), y configurar las credenciales requeridas como `Basic Auth`en la pestaña `authorizations`

![](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/PostmanInstructions.png)

**Nota**: como se está utilizando `Basic Auth`, es recomendable almacenar las credeciales como variables dentro de un ambiente de Postman, en lugar de declararlas en cada una de las request.

 
# Posible mejoras
Algunas de las posibles mejoras para la versión actual son:

* Agregar mayor funcionalidad a las clases, como por ejemplo:
  	* Poder setear responsables para cada tarea
  	* Porder establecer/calcular el porcetaje de completitud de cada tarea.
  	* Poder establecer tipos y prioridades para las sub tareas.
  	* Poder establecer tamaños para las subtareas.
  	* Etc
  	  
* Mejorar la gestión de usuarios y la seguridad:
  	* ***Usar SSL sobre HTTP***
  	* Hacer obligatoria una verificación del mail por parte de los usuarios.
  	* Setear tiempo de expiración para las contraseñas.
  	* Generar mejores chequeos para evitar ataques del tipo: XSSm SQLi, CRFF, entre otros.

* Investigar formas de mejorar la performace de la aplicación tales como: usar prefetch para las queries, paginación y otras.
* Añadir pre-commits hooks, para garantizar el estilo de código
