#!/bin/bash

# Exit on error
set -e

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Apply migrations
echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python manage.py auto_createsuperuser --username admin --email admin@example.com --password admin

# Create additional users
echo "Creating additional users..."
python manage.py auto_createtestusers --users 5

# Display documentation links
echo "______________________________________________________________________"
echo "API Documentation Links:"
echo "Swagger UI: http://127.0.0.1:8000/swagger/"
echo "ReDoc: http://127.0.0.1:8000/redoc/"
echo "Admin User: usr: admin, pass: admin"
echo "______________________________________________________________________"

# Run the server
echo "Starting development server..."
python manage.py runserver
