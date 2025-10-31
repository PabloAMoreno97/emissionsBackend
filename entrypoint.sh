#!/bin/bash
# entrypoint.sh
set -e

python manage.py seed_emission.py --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"