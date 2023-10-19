#!/usr/bin/env sh
set -e

dockerize -wait tcp://db:5432

./manage.py migrate --noinput
./manage.py collectstatic --noinput
./manage.py load_cities
./manage.py bot_start

exec "$@"
