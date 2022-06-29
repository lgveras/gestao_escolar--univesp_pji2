release: python manage.py migrate
release: python manage.py seed_db --mode=refresh
web: gunicorn gestao_escolar.wsgi