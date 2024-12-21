COMPOSE = docker compose
SERVICE = web


build:
	$(COMPOSE) build

build-no-cache:
	$(COMPOSE) build --no-cache $(SERVICE)

up:
	$(COMPOSE) up

up-d:
	$(COMPOSE) up -d

prune:
	docker volume prune -f

shell:
	$(COMPOSE) exec $(SERVICE) python manage.py shell

bash:
	$(COMPOSE) exec -it $(SERVICE) bash

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
