#!/bin/bash

echo "Makemigratins..."
python manage.py makemigrations
sleep 1

echo "Migrate..."
python manage.py migrate
sleeep 1

echo "requirements writing..."
pip freeze > ../requirements.txt

echo "Running on 9000 port... "
python manage.py runserver
