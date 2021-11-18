COMPOSE = docker compose
SERVICE = web


build:
	$(COMPOSE) build

up:
	$(COMPOSE) up

createsuperuser:
	$(COMPOSE) exec $(SERVICE) python manage.py createsuperuser

test:
	$(COMPOSE) run --rm $(SERVICE) pytest -vv

down:
	$(COMPOSE) down

migrate:
	$(COMPOSE) exec $(SERVICE) python manage.py migrate

migrations:
	$(COMPOSE) exec $(SERVICE) python manage.py makemigrations

showmigrations:
	$(COMPOSE) exec $(SERVICE) python manage.py showmigrations
