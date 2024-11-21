build command: pip install -r requirements.txt && python manage.py collectstatic --noinput
start command (production): gunicorn config.wsgi:application --bind 0.0.0.0:$PORT

"    category sales\n0          A   300\n1          B   150\nAlong with a bar plot showing total sales for each category"