#!/bin/bash

# curl -X post  $HOST:$PORT/api/v1/rest-auth/registration/ \
#  -H 'Content-Type: application/json' \
#  -d '{ 
#   "username": "leof", 
#   "email": "ali@ff.com", 
#   "password1": "leoleoleo", 
#   "password2": "leoleoleo"
#   }'

# curl -X post  $HOST:$PORT/api/v1/rest-auth/login/ \
# -H 'Content-Type: application/json' \
# -d '{
#   "username": "aliakbar", 
#   "password": "aliakbar"
# }'
HOST=localhost
PORT=8000
TOKEN='5a09226ddad924bd790a4f2fdae4f10ec408d2bc'
AUTH_HEADER="Authorization: Token $TOKEN"

curl -X get $HOST:$PORT/api/v1/author/ \
-H "$AUTH_HEADER"

curl -X post $HOST:$PORT/api/v1/author/ \
-H 'Content-Type: application/json' \
-d '{
  "name": "leboef",
  "password": "pass",
  "username": "leo"
}'

curl -X get $HOST:$PORT/api/v1/blogpost/ \
-H "$AUTH_HEADER"

curl -X post $HOST:$PORT/api/v1/blogpost/ \
-H "$AUTH_HEADER" \
-H 'Content-Type: application/json' \
-d '{
  "title": "leo44nino",
  "author": 3,
  "body": "the best in the world"
}'

export ADMIN_USER='aliakbar'
export ADMIN_EMAIL='lo@gmail.com'
export ADMIN_PASSWORD='aliakbar'

export MYSQL_DB='qops_blog'
export MYSQL_USER='aliakbar'
export MYSQL_PASS='sesame'
export MYSQL_PORT='3306'
export MYSQL_HOST='localhost'
export MYSQL_READ_HOST='localhost'
export MYSQL_WRITE_HOST='localhost'
./manage.py runserver
source /home/aliakbar/tech/django-paas/venv/bin/activate
