web: gunicorn PROJECT.wsgi
worker: celery -A PROJECT worker
beat: celery -A PROJECT beat
celeryworker: celery -A PROJECT worker & celery -A PROJECT beat & wait -n