# FutureValue Calculator

A Django web application for calculating future values with an intuitive web interface. This project provides a simple calculator tool built using Django framework with a clean frontend design.

## Project Structure

The project follows Django's standard structure with a main project directory and a calculator app:

- **FutureValue/**: Main Django project directory containing configuration files
- **calculator/**: Django app handling the calculator functionality
- **static/**: Static files (CSS, JavaScript) for frontend styling and interactions
- **templates/**: HTML templates for the web interface

## Features

- Future value calculations through a web interface
- Clean and responsive design
- JavaScript-powered calculator functionality
- Django admin interface support

## Requirements

- Python 3.x
- Django 3.x or higher
- Web browser for accessing the application

## Installation & Setup

### 1. Clone or Download the Project
```bash
git clone 
cd FutureValue
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Django
```bash
pip install django
```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

## Running the Application

### Start Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Access Admin Panel
If you created a superuser, access the admin panel at `http://127.0.0.1:8000/admin/`

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`
2. Use the calculator interface to input values
3. Calculate future values based on your inputs
4. View results on the same page

## Development Commands

### Check for Issues
```bash
python manage.py check
```

### Create New Migrations (if models are modified)
```bash
python manage.py makemigrations
```

### Run Tests
```bash
python manage.py test
```

### Shell Access
```bash
python manage.py shell
```

## File Organization

- `manage.py`: Django's command-line utility
- `settings.py`: Project configuration
- `urls.py`: URL routing configuration
- `views.py`: Application logic and request handling
- `models.py`: Database models (if any)
- `templates/calculator/index.html`: Main calculator interface
- `static/calculator/css/style.css`: Styling for the calculator
- `static/calculator/js/calculator.js`: JavaScript functionality

## Customization

To modify the calculator:
- Edit `calculator/views.py` for backend logic
- Update `templates/calculator/index.html` for HTML structure
- Modify `static/calculator/css/style.css` for styling
- Enhance `static/calculator/js/calculator.js` for frontend functionality

## Troubleshooting

- Ensure Python and Django are properly installed
- Check that all migrations are applied
- Verify static files are collected
- Make sure the virtual environment is activated
- Check Django version compatibility

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
