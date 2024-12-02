#!/bin/bash
 
# Create a virtual environment
echo "Creating a virtual environment..."
python3.12 -m venv venv
source venv/bin/activate
 
# Install the latest version of pip
echo "Installing the latest version of pip..."
python -m pip install --upgrade pip
 
# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt
 
# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear
 
# cada vez que suba un cambio nuevo esto escribe esos cambios en la base de datos de neon
echo "Sync database..."
python manage.py migrate
 
# le decimos que ejecute ciertos comandos (python manage.py seeds)
echo "Superuser..."
python manage.py seeds