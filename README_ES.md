
# Invera Todo Challenge

Este repositorio contiene la primera version del challenge de Invera (Python/Django Jr-SSr). Todos los detalles referentes a este defaío y sus requerimientos pueden ser encontrados [aquí](https://github.com/invera/todo-challenge?tab=readme-ov-file).

# Resumen del desarrollo realizado.
El objetivo principal de este desarrollo, es cumplir con los objetivos establecidos por el desafío. Por esta razón se desarrollo una pequeña aplicación, cuya estructura es muy simple, cuenta con 3 diferentes modelos (clases) que permitir a los usuarios agendar tareas para ser completadas.

Las clases son:

 - User
 - Task
 - Subtask

Los siguientes son los diagramas de Clases y E/R pensados para la aplicación:

![Diagram 1](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/Diagrama1.png)
![Diagram 2](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/Diagrama2.png)


# Como correr la aplicación.
Lo primero que se requiere es clonar el repositorio en máquina local. Esto puede realizarse ejecutando el siguiente comando `git clone git@github.com:pereza94/todo-challenge.git` situandose dentro de la carpeta donde desea que el proyecto sea alojado.

Una vez hecho esto, es posible elegir entre 2 opciones para correr la aplicacion:
* Usando docker
* Creando su propio entorno virtual.

### Opcion A: Usando Docker
Una forma muy simple de probar el funcionamiento de la aplicación, es ejecutando la misma dentro de un Docker. Para esto es necesario contar con la aplicación `Docker Desktop` instalada en la computadora donde se buildeara el contenedor (en caso de contar la aplicación, la misma puede ser descargada desde [docker site](https://www.docker.com/products/docker-desktop/#).

Para verficar que la instalaciñon fue exitosa, puede correr en su terminal el comando `command docker --version`. Si como resultado se muestra la version de Docker, el programa fue instalado exitosamente.
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_version.png?token=GHSAT0AAAAAACOYVBDTPXDGZCPSWUHIRJ7EZPHNKMQ)

Llegados a este punto, solo es necesario buildear el contenedor. Para esto asegurese que se encuentra en la carpeta correcta (debería ver las carpetas 'tasks', 'tests', ' todoChallenge' entre otras, y un archivo llamado `DockerFile`), y correr el siguiente comando `docker build -t todochallenge .`. Una vez finalizada la construcción del Docker, verá una imagen similar a la siguiente:

![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_build.png?token=GHSAT0AAAAAACOYVBDS3YBN4OURILOUBBCSZPHOJQA)

Seguidamente es necesario ejecutar el docker, con la siguiente instrucción:
` sudo docker run -it -p 9000:8000 todochallenge`
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_running.png?token=GHSAT0AAAAAACOYVBDSKMTOS5K6XBZXIDWOZPHOIWQ)
*Nota: en el ejemplo, la máquina local está escuchando en el puerto 9000, pero es posible elegir cualquier puerto que desee*

Finalmente, si todo salió bien, debería ver la documentación de swagger al visitar la URL:http://localhost:9000/swagger/docs/.

### Option B: Installing your own virtual environment

The first step is to create a virtualenv, one easy way to do that is using the tool `mkvirtualenv`. This tool is available [here](https://virtualenvwrapper-docs-es.readthedocs.io/es/latest/install.html).

To create the venv you can use the following command:
`mkvirtualenv --python=python3.8 invera-challenge`

Once you are in the Repo folder,  you need to install all the necessary dependencies, to do that you can run the following
`pip install -r requirements.txt`

Finally you can run the following to run the App:
` python manage.py runserver` 
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/django-running-in-venv.png?token=GHSAT0AAAAAACOYVBDSQY4HOOUXBQ3IPWGKZPHPOCA)

*Note:  by default, django starts the server listening in port 8000. But if you need to modify it is possible passing it as an argument in the command, for example `python manage.py runserver 0.0.0.0:8080`*

If everything goes well you should be able to check the app documentation in  http://localhost:8080/swagger/docs/.
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/swagger-documentation.png?token=GHSAT0AAAAAACOYVBDSNPE7XZADIFDNOJA2ZPHPRGA)


# How to interact with App
Once the App is running, it is possible to interact with it using requests. Currently exists many different tools that allow making requests in a straightforward mode.

The App is running swagger, in the route `/swagger/docs`. This page displays all the possible interactions that are currently available, and by setting the proper credentials you can make as many requests as you want.

There is a super user available to be used whose username and password are **challenge:ChallengePassword**
 ![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/swagger-image.png)

In the route `tasks/task` the one that allows listing all the tasks stored in the DB, there are the following filters:

 - ***description_contains***: returns all the tasks whose description contains the searched text.
 - ***name_contains***: returns all the tasks whose name contains the searched text.
 - ***minimum_date***: returns all the tasks created after the date set. (The expected input format is dd-mm-yy)
 - ***maximum_date***: returns all the tasks created before the date set. (The expected input format is dd-mm-yy)

## Interacting using postman

Another option to interact with the App is using Postman. To do that it is possible to use this [collection](https://github.com/pereza94/ImagesForReadmes/blob/draft/TodoChallenge.postman_collection.json), and set the required credentials as `Basic Auth` in the authorizations tab.

![](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/PostmanInstructions.png)

***Note***: as Basic Auth is being used, it is highly recommended to save it as variables inside a Postman environment, instead of setting it in the request itself.

 
# Posible Improvements
Some of the possible improvements for the current version are:

* Add more functionality to classes, like: 
	* Be able to set responsibilities for each task.
	* Be able to set a percentage of task progress
	* Be able to set priority and types for subtasks
	* Be able to set a task size
	* Etc

* Improve user manage and security:
	*  ***Use SSL over HTTP***
	* Make mandatory a user mail verification.
	* Set user's password expiration
	* Make better checks to avoid attacks of type: *XSS, SQLi, CRSF* and others.
	* Add internal logging, and not only transactions login

* Look for methods to improve the performance like, prefetch the queries, paginated, and others.
