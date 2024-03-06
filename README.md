`Este README esta disponible en español` [aquí](https://github.com/pereza94/todo-challenge/blob/develop/README_ES.md)
# Invera Todo Challenge

This Repo contains the first version of Invera's challenge (Python/Django Jr-SSr).  All the details about the challenge and its requirements can be found [here](https://github.com/invera/todo-challenge?tab=readme-ov-file).

# Development summary
The main objective of this development is to comply with the requirements of the challenge. For that reason a small application was developed, the structure is really simple, where interact 3 different models (classes) to allow the users to book pending tasks.

The classes are:

 - User
 - Task
 - Subtask

The following are the Classes and E/R diagrams

![Diagram 1](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/Diagrama1.png)
![Diagram 2](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/Diagrama2.png)

# How to run this App.
The first thing you need to do is clone this repo in your machine. To do that is just necessary to execute the command `git clone git@github.com:pereza94/todo-challenge.git` inside the folder where you want the Repo to be cloned in your computer. 

Once this is completed, you can take two different ways to run the App:

 - Using Docker (suggested if you only need to run and use the APP)
 - Creating your virtual enviromment (suggested if you wish to make contributions and maintain the APP)

### Option A: Using Docker
The simplest way to run this App for testing its behavior is using Docker. To use docker it is necessary to install on the local machine the Docker Desktop (if you don't have the tool already installed, you can download it from [docker site](https://www.docker.com/products/docker-desktop/#), the tool is available for mostly all popular SO)

To check if the docker was properly installed, you run in your terminal (or Powershell if you are using Windows) the command docker --version. If you received the version as output means that docker was installed successfully.

![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_version.png?token=GHSAT0AAAAAACOYVBDTPXDGZCPSWUHIRJ7EZPHNKMQ)


At this point, you only need to go to the folder where the Repo was cloned. To be sure that you are in the right folder, you should  view at least the following folders `tasks, test, todoChallenge` and a file named `DockerFile`

Once there you need to build the docker image, by running the following command:
`docker build -t todochallenge .`. When the image building is finished, you will see a message similar to the following one:
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_build.png?token=GHSAT0AAAAAACOYVBDS3YBN4OURILOUBBCSZPHOJQA)

Next, you need to run the docker with the following instructions:
` sudo docker run -it -p 9000:8000 todochallenge`
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_running.png?token=GHSAT0AAAAAACOYVBDSKMTOS5K6XBZXIDWOZPHOIWQ)
*Note:  in the former example, the local machine is listening in port 9000, but you could whatever port that you want*

Finally, if everything was as expected, you should be able to access the swagger documentation visit in your browser at the following url: http://localhost:9000/swagger/docs/.

### Option B: Installing your own virtual environment

The first step is to create a virtualenv, one easy way to do that is using the tool `mkvirtualenv`. This tool is available [here](https://virtualenvwrapper-docs-es.readthedocs.io/es/latest/install.html).

To create the venv you can use the following command:
`mkvirtualenv --python=python3.8 invera-challenge`

Once you are in the Repo folder,  you need to install all the necessary dependencies, to do that you can run the following
`pip install -r requirements.txt`

Finally, you can run the following to run the App:
` python manage.py runserver` 
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/django-running-in-venv.png?token=GHSAT0AAAAAACOYVBDSQY4HOOUXBQ3IPWGKZPHPOCA)

*Note:  by default, django starts the server listening in port 8000. But if you need to modify it is possible to pass it as an argument in the command, for example `python manage.py runserver 0.0.0.0:8080`*

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
* Add pre-commit hooks to guarantee the code style
