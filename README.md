- ASGI (Asynchronous Server Gateway Interface)
- WSGI (Web Server Gateway Interface)

## Command

Create virtual environment
```sh```
py -m venv [ven_name]
source [ven_name]/bin/active (for Mac)
source [ven_name]\Scripts\Activate.ps1 (for Windows)
```sh```

Run server
```sh```
py manage.py runserver
```sh```

Database Migration
```sh```
py manage.py migrate
```sh```

Create Superuser and Log in to Django Admin
```sh```
py manage.py createsuperuser
```sh```

Start app
```sh```
py manage.py startapp [appname]
```sh```

## Chapter 3. Django Models and Database

Step
1. Create Django Models by editing models.py
2. Make a migration file by running the `makemigration` command
3. Create database tables by running the `migrate` command

Then register Models in Django Admin - admin.py

```sh```
admin.site.register(models_name)
```sh```