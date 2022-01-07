web: gunicorn PROJECT.wsgi
worker: celery -A PROJECT worker
beat: celery -A PROJECT beat