- ASGI (Asynchronous Server Gateway Interface)
- WSGI (Web Server Gateway Interface)

## Command

Create and active virtual environment. Remember active for running any command
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
py manage.py makemigrations [app_name]
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

- config/urls.py is defined urlpatterns to route app

Example

```sh```
(dj_env) PS D:\gymcoding\gymcoding_django> py manage.py makemigrations employee_learning
Migrations for 'employee_learning':
  employee_learning\migrations\0005_employee_reg_date.py
    - Add field reg_date to employee

(dj_env) PS D:\gymcoding\gymcoding_django> py manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, employee_learning, sessions
Running migrations:
  Applying employee_learning.0005_employee_reg_date... OK

  ... and check on http://127.0.0.1:8000/admin/employee_learning/employee/
```sh```

Foreign Key (OneToMany Relationship)

```sh```
models.ForeignKey(RelatedModel, on_delete=xx)
```sh```

Three possible values for `on_delete` argument:
- CASCADE: deletes the obbject containing the ForeignKey
- PROTECT: prevents deletion of the referenced object by raising ProtectedError
- RESTRICT: prevents deletion of the referenced object by raising RestrictedError