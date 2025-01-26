#!/bin/bash

# Exit on error
set -e

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv_local 

# Activate virtual environment
echo "Activating virtual environment..."
source venv_local/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Apply migrations
echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
EOF

# Create additional users
echo "Creating additional users..."
python manage.py shell <<EOF
from users.models import User
for i in range(1, 6):
    User.objects.create(name=f'User {i}')
EOF

# Run the server
echo "Starting development server..."
python manage.py runserver

# Display documentation links
echo "\nAPI Documentation Links:"
echo "Swagger UI: http://127.0.0.1:8000/docs/swagger/"
echo "ReDoc: http://127.0.0.1:8000/docs/redoc/"