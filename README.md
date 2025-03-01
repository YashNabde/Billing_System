# Billing System

## Overview
This is a Django-based **Billing System** that allows users to create, manage, and generate invoices efficiently. The system provides an easy-to-use interface for handling billing operations, including customer management, invoice generation, and payment tracking.

## Features
- **User Authentication**: Secure login/logout functionality.
- **Invoice Management**: Create, edit, and delete invoices.
- **Customer Management**: Store customer details for recurring billing.
- **Automated Invoice Generation**: Generates invoices dynamically.
- **Django Admin Panel**: Manage all records via Django's built-in admin interface.
- **Database Storage**: Uses SQLite (default) or PostgreSQL/MySQL for data persistence.

## Technologies Used
- **Python 3.11**
- **Django**
- **SQLite / PostgreSQL / MySQL**
- **HTML, CSS, Bootstrap (for frontend)**
- **JavaScript (if applicable)**

## Installation
### Prerequisites
Ensure you have **Python** and **pip** installed:
```sh
python --version
pip --version
```
### Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/Billing_System.git
cd Billing_System
```
### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
```
### Install Dependencies
```sh
pip install -r requirements.txt
```
### Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
### Create a Superuser
```sh
python manage.py createsuperuser
```
Follow the prompt to set up an admin user.

### Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/admin/` to access the admin panel.

## Usage
1. Login to the admin panel and add customers.
2. Generate invoices and manage billing records.
3. Track payments and due invoices.
4. Export or print invoices as needed.

## Troubleshooting
If you face migration issues, run:
```sh
python manage.py migrate --fake-initial
```
To check for registered models in Django Admin:
```sh
python manage.py shell
from django.contrib import admin
print(admin.site._registry)
```
## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is currently unlicensed.

## Contact
For any issues, feel free to reach out:
- **GitHub**: YashNabde
- **Email**: yashn3428@gmail.com
