#!/usr/bin/env bash
# exit on error
# set -o errexit

# poetry install


python manage.py collectstatic --no-input
python manage.py migrate

# python manage.py runserver 0.0.0.0:8000
gunicorn PROJECT.wsgi:application --bind