# Dockerfile

# We Use an official Python runtime as a parent image
FROM python:3.8

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
#ENTRYPOINT ["python", "todoChallenge/todoChallenge/manage.py"]
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]