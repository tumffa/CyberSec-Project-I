#!/bin/bash

# Step 1: Apply the database migrations
python manage.py migrate

# Step 2: Configure the database with users and their messages
python manage.py configure_db

# Step 3: Run the Django development server
python manage.py runserver