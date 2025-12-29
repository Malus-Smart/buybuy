#!/bin/bash
echo "Running database migrations..."
python manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Starting Gunicorn..."
exec gunicorn buybuy.wsgi --log-file -

