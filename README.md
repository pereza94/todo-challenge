#
# Invera Todo Challenge

This repo contains the very first version of  Invera's challenge (Python/Django Jr-SSr).  All the details about the challenge and its requirements can be found [here](https://github.com/invera/todo-challenge?tab=readme-ov-file).

# Development Scope
TODO: here I must add the UML diagrams and explain the future improvements

# How to run this App.
The first thing you need to do is clone this repo in your local enviromment. To do that is just necessary to execute the command `git clone git@github.com:pereza94/todo-challenge.git` inside the folder where you want the Repo to be cloned in your computer. 

Once this is completed, you can take two different ways to run the App:

 - Using Docker (suggested if you only need to run and use the APP)
 - Creating your virtual enviromment (suggested if you wish to make contributions and maintain the APP)

### Option A: Using Docker
The simplest way to run this App for testing its behavior is using Docker. To use docker it is necessary to install on the local machine the Docker Desktop (if you don't have the tool already installed, you can download it from [docker site](https://www.docker.com/products/docker-desktop/#), the tool is available for mostly all popular SO)

To check if the docker was prpoperly installed, you run in your terminal (or Powershell if you are using Windows) the command docker --version. If you received the version as output means that docker was installed successfully.

![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_version.png?token=GHSAT0AAAAAACOYVBDTPXDGZCPSWUHIRJ7EZPHNKMQ)


At this point, you only need to go to the folder where the Repo was cloned. To be sure that you are in the right folder, you should  view at least the following folders `tasks, test, todoChallenge` and a file named `DockerFile`

Once there you need to build the docker image, running the following command:
`docker build -t todochallenge .`. When the image building is finished, you will see a message similar to the following one:
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/docker_build.png?token=GHSAT0AAAAAACOYVBDS3YBN4OURILOUBBCSZPHOJQA)

Next, you need to run the docker with the following instruction:
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

Finally you can run the following to run the App:
` python manage.py runserver` 
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/django-running-in-venv.png?token=GHSAT0AAAAAACOYVBDSQY4HOOUXBQ3IPWGKZPHPOCA)

*Note:  by default django starts the server listening in port 8000. But if you need to modify it is possible passing it as argument in the command, for example `python manage.py runserver 0.0.0.0:8080`*

If everything goes well you whould be able to check the app documentation in  http://localhost:8080/swagger/docs/.
![enter image description here](https://raw.githubusercontent.com/pereza94/ImagesForReadmes/draft/swagger-documentation.png?token=GHSAT0AAAAAACOYVBDSNPE7XZADIFDNOJA2ZPHPRGA)






