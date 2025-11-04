#!/bin/sh
set -e

python manage.py migrate --noinput

python manage.py seed_emissions || true

gunicorn --bind 0.0.0.0:8000 config.wsgi:application