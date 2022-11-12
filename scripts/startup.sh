#!/bin/bash

echo "Start performing migrations"

python manage.py migrate --noinput

echo "Collect static files"

python manage.py collectstatic --noinput

echo "Start gunicorn [wsgi] application"

gunicorn --workers 2 -b "0.0.0.0:8310" --threads 2 config.wsgi