FROM python:3.9-slim-buster
LABEL authors="sunny"
RUN apt-get update
RUN apt-get install -y python-dev default-libmysqlclient-dev build-essential pkg-config
RUN pip install mysqlclient
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver