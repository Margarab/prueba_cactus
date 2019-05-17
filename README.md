# Prueba conocimiento WE ARE CACTUS

## Set Up
Install system requirements (Ubuntu-based distributions)

    $ sudo apt-get update
    $ sudo apt-get install python3-dev libpq-dev

Clone repository and install requirements with:

    $ pip install -r requirements.txt

Migrate database

    $ python manage.py migrate

Load fixture

    $ python manage.py loaddata fixture.json

Go to repository_directory and launch server:

    $ python manage.py runserver



## Users
> Login as admin

    user: admin@admin.com  password:plokijuh

User admin have permission to list, create and update users


> Login as user

    user: user1@user.com  password:plokijuh

Users client only have permissions to retrieve and update own profile

## Environment
It's required to create a .env file in root. A .env.example file is provided

| Environment variable  | Default                                       |
|-----------------------|-----------------------------------------------|
| `DEBUG`               | True                                          |
| `SECRET_KEY`          | abcd                                          | 
| `DATABASE_URL`        | postgres://user:password@server:port/db_name  |
| `ALLOWED_HOSTS`       | []                                            |

## Sitemap
API REST with [Django REST Framework](http://www.django-rest-framework.org/)

    - / : Api Root
    - /users/ : Users List (Only for admin)
    - /users/<username>/ : User detail
    - /admin/ : Django admin
    - /api-auth/login/ : Login with rest
    - /accounts/google/login : Login with Google
    
## Allauth
Enabled google login through `django-allauth`




