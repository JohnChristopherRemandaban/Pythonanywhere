# Task Manager / To-Do App

A feature-rich task management application built with Django that helps users organize their tasks with categories and track their progress.

## Features

- **User Authentication**
  - Secure user registration and login
  - Personal task management space for each user

- **Task Management**
  - Create, edit, and delete tasks
  - Add detailed descriptions and due dates
  - Track task status (Pending, In Progress, Done)
  - Categorize tasks for better organization

- **Category System**
  - Create custom categories (e.g., Work, Personal)
  - Organize tasks by categories
  - View task count per category

- **User Interface**
  - Clean and responsive Bootstrap-based design
  - Intuitive navigation
  - Status indicators with color coding
  - User-friendly forms

## Technology Stack

- Python 3.11
- Django 4.x
- Bootstrap 5.1
- SQLite (default database)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task-manager-todo-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Install required packages:
   ```bash
   pip install django
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at:
   - Main app: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin

## Usage

1. **Login/Register**
   - Create a new account or login with existing credentials
   - Admin users can access the admin interface

2. **Managing Categories**
   - Create categories to organize your tasks
   - View task count for each category

3. **Task Operations**
   - Create new tasks with title, description, and due date
   - Assign tasks to specific categories
   - Update task status as they progress
   - Edit or delete tasks as needed

## Project Structure

```
task_manager/
├── manage.py
├── task_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todo/
    ├── migrations/
    ├── templates/
    │   └── todo/
    │       ├── base.html
    │       ├── task_list.html
    │       ├── task_form.html
    │       ├── category_form.html
    │       └── login.html
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── forms.py
    └── urls.py
```

## Security

- All views are protected with login required decorator
- Users can only access and modify their own tasks and categories
- CSRF protection enabled for all forms
- Secure password hashing using Django's authentication system

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for any bugs or feature requests.

## License

This project is open source and available under the [MIT License](LICENSE).
