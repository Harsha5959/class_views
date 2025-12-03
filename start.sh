python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn class_views_project.wsgi:application --bind 0.0.0.0:$PORT 