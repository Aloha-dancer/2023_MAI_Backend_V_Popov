FROM python:3.8

ENV DJANGO_SETTINGS_MODULE game_shop.docker_settings
RUN pip install --upgrade pip
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
