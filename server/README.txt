build command: pip install -r requirements.txt && python manage.py collectstatic --noinput
start command (production): gunicorn config.wsgi:application --bind 0.0.0.0:$PORT