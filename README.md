# JWT-Based Authentication Django Project

A Django-based project that implements JWT authentication and role-based access control for managing blogs and likes. This project also includes custom permissions to control access and editing capabilities.

## Features

- **User Roles**: Users can be regular users, authors, or admins.
- **JWT Authentication**: Secure user authentication with token-based mechanisms.
- **Role-Based Access Control**:
  - Admins can grant or revoke permissions for authors.
  - Authors can create and manage blogs.
  - Users can like and unlike blogs.
- **Blog Management**: CRUD operations for blogs with permission-based access.
- **Custom Permissions**: Fine-grained control over user actions, including blog editing and liking.
- **Like Counting**: Blogs display the number of likes.

## Prerequisites

- Python 3.8+
- Django 4.x
- Django REST Framework
- PostgreSQL or any preferred database
- `djangorestframework-simplejwt` for JWT implementation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fazi160/jwt-based-auth-django.git
   cd jwt-based-auth-django
   ```
2. Create and activate a virtual environment:

   ```bash

   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```



4. Apply migrations:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

5. Create a superuser:

  ```bash
  python manage.py createsuperuser
  ```
6. Start the development server:
  ```bash
  python manage.py runserver
```

API Endpoints
Authentication
* Login: /login/ (POST)
* Token Refresh: /refresh/ (POST)

User Management
* Create User: /users/create/ (POST)
* Grant/Revoke Permission: /users/admin_author/ (POST)
  
Blog Management
* List Blogs: /blog/ (GET)
* Retrieve Blog: /blog/<id>/ (GET)
* Create Blog: /blog/ (POST)
* Update Blog: /blog/<id>/ (PUT/PATCH)
* Delete Blog: /blog/<id>/ (DELETE)
  
Blog Likes
* Like/Unlike a Blog: /like_blog (POST)

Project Structure
```bash

jwt-based-auth-django/
├── blogs/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── permissions.py
├── .gitignore  # Git ignore file
├── db.sqlite3  # Default SQLite database (or your chosen database)
├── manage.py  # Django management script
├── requirements.txt  # Python dependencies
```

Usage
Register a new user via the /users/create/ endpoint.
Log in using the /login/ endpoint to get a JWT token.
Use the JWT token in the Authorization header for protected endpoints.
Admins can manage permissions using /users/admin_author/.
Authors can create, edit, or delete blogs, and users can read, like/unlike blogs.
