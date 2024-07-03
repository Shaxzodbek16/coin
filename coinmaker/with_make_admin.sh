#!/bin/bash

python manage.py createsuperuser

sleep 2
echo "Running......."

./runner.sh
