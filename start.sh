#!/bin/bash
#TODO: make the script better: check if the superuser exists

./manage.py makemigrations blog 
./manage.py makemigrations 
./manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')" \
| ./manage.py shell
./manage.py runserver 0.0.0.0:8000