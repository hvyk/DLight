#!/usr/local/bin/bash
rm db.sqlite3 icecream/migrations/0*
python manage.py makemigrations
python manage.py migrate