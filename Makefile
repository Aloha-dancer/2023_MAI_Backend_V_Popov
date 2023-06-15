start:
	docker-compose build & docker-compose up -d

migration:
	docker-compose run --rm django sh -c "python3 DockerDjango/manage.py makemigrations"
	docker-compose run --rm django sh -c "python3 DockerDjango/manage.py migrate"


test: