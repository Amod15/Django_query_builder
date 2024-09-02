# Catalyst Count

Catalyst Count is a Django-based web application designed for efficient data management and user authentication. It enables users to upload large CSV files, process them asynchronously, and store the data in a PostgreSQL database. The application features a responsive user interface, secure environment configuration, and user authentication.

## Table of Contents

- [Project Setup](#project-setup)
- [Database Configuration](#database-configuration)
- [Environment Configuration](#environment-configuration)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Setup

### Prerequisites

- Python
- PostgreSQL
- Virtualenv

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/catalyst-count.git
    cd catalyst-count
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv_name
    source venv_name/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt  ---i have added this file on git repository
    ```

4. **Set up the Django application**:
    ```bash
    python manage.py migrate 
    python manage.py runserver
    python manage.py createsuperuser -- for creating users for login
    ```


## Database Configuration

1. **PostgreSQL Setup**:
    - Install PostgreSQL on your system.
    - Create a database named `catalyst_emp_count`.

2. **Database Configuration in Django**:
    - Update the `.env` file with the following configuration:
    ```ini
    DATABASE_URL=postgres://myuser:root@localhost:5432/catalyst_emp_count
    DB_PASSWORD='root'
    ```

3. **Model Schema**:
    - Create models in `models.py` based on the provided test dataset.
    - Run migrations to apply the schema to the PostgreSQL database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Environment Configuration

1. **Environment Variables**:
    - Install `django-environ` to manage environment variables securely:
    ```bash
    pip install django-environ
    ```

    - Create a `.env` file in the project root with the following variables:
    ```ini
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=postgres://myuser:root@localhost:5432/catalyst_emp_count
    DB_PASSWORD='root'
    ```

2. **Settings Configuration**:
    - Modify `settings.py` to read from the `.env` file:
    ```python
    import environ

    env = environ.Env()
    environ.Env.read_env()

    DEBUG = env.bool('DEBUG', default=False)
    SECRET_KEY = env('SECRET_KEY')
    DATABASES = {
        'default': env.db()
    }
    ```

## Features

- **User Authentication**: Secure login and registration using Django Allauth.
- **File Upload**: Upload large CSV files (up to 1GB) with a visual progress bar.
- **Responsive UI**: Built with Django templates and Bootstrap 4 for a modern and intuitive interface.

## Usage

1. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

2. **Access the Application**:
    - Open your browser and go to `http://localhost:8000/`.
    - Log in using the superuser credentials you created during setup.

3. **Upload CSV Files**:
    - Navigate to the "Upload Data" section.
    - Upload your CSV file and monitor the progress via the progress bar.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.


