#!/bin/sh
sleep 15

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn app.wsgi:application --bind 0.0.0.0:3000