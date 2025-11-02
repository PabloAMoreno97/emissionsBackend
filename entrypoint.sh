#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Seeding data..."
python manage.py seed_emissions || true

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
