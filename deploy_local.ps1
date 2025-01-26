# Exit on error
$ErrorActionPreference = "Stop"

# Create virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate

# Install dependencies
Write-Host "Installing dependencies..."
pip install -r requirements.txt

# Apply migrations
Write-Host "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
Write-Host "Creating superuser..."
Python manage.py auto_createsuperuser --username admin --email admin@example.com --password admin

# Create additional users
Write-Host "Creating additional users..."
Python manage.py auto_createtestusers --users 5

# Display documentation links
Write-Host "______________________________________________________________________"
Write-Host "`nAPI Documentation Links:"
Write-Host "Swagger UI: http://127.0.0.1:8000/docs/swagger/"
Write-Host "ReDoc: http://127.0.0.1:8000/docs/redoc/"

Write-Host "Admin User: usr: admin, pass: admin"
Write-Host "______________________________________________________________________"
# Run the server
Write-Host "Starting development server..."
python manage.py runserver

