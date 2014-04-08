Django 1.6 Project Layout Template
==================================

Template to use to lay out a Django 1.6 project.
Follow the steps in order to create a new Django 1.6 project with a similar layout.


LOCAL DEVELOPMENT
-----------------

### 1. Create a project folder in your workspace
    $ mkdir icecreamshop-project
    $ cd icecreamshop-project
We will refer to this folder as *repository root*.


### 2. Create a virtual environment
We use Virtualenvwrapper.

    $ mkvirtualenv icecreamshop
Or:

    $ mkvirtualenv -p /usr/bin/python2.7 icecreamshop

Next set the right settings file and passwords as environment variables.
Virtualenvwrapper hook on activation:

    $ nano ~/.virtualenvs/icecreamshop/bin/postactivate
    # Settings
    export DJANGO_SETTINGS_MODULE=icecreamshop.settings.local

    # Passwords
    export MY_SECRET="my_secret_password"

Virtualenvwrapper hook on deactivation:

    $ nano ~/.virtualenvs/icecreamshop/bin/predeactivate
    # Settings
    unset DJANGO_SETTINGS_MODULE

    # Passwords
    unset MY_SECRET

Optionally make a copy of the environment variables (the passwords) in the file:
    `icecreamshop/icecreamshop/settings/vars.environment`
This file will be IGNORED by Git, so it will be stored only in your local machine.
You might need it in case you accidentally remove your virtual environment and lose your passwords.

Reactivate the virtual environment:

    $ deactivate
    $ workon icecreamshop


### 3. Install Django
    $ pip install django


### 4. Create the Django project
    $ django-admin.py startproject icecreamshop
This will create the folder icecreamshop with basic Django files.
We will refer to this folder as *Django project root*.
Inside this folder Django creates another folder named again icecreamshop with the settings and wsgi files and the URLConf.
We will refer to this folder as *configuration root*.


### 5. Create settings and requirements files in the configuration root
    $ cd icecreamshop/icecreamshop
    $ mkdir requirements
    $ mkdir settings
    $ mv settings.py settings/base.py


### 6. Edit requirements
In the requirements folder create the requirements files by copying those here.


### 7. Edit settings
In the settings folder edit base.py by looking at the base.py here.
Notice the lines with `# EDIT:`: those are the changes to the default.
In particular in base.py:
- change BASE_DIR to one dir up
- set the secret key to '0'
- add south to INSTALLED_APPS
- set the static folder

Create a `static` folder in *Django project root*:

    $ mkdir static

And add to the main urls.py the settings for debug_toolbar:

    ```python
    from django.conf import settings
    if settings.DEBUG:
        import debug_toolbar
        urlpatterns += patterns('',
            url(r'^__debug__/', include(debug_toolbar.urls)),
        )


### 9. Install the requirements
    $ workon icecreamshop
    $ pip install -r icecreamshop/requirements/local.txt


### 10. Create the db
    $ python manage.py syncdb --migrate


### 11. Run the server
    $ python manage.py runserver_plus


### 12. Create the first app
    $ python manage.py startapp accounts

Add some models and create a migration:

    $ python manage.py schemamigration accounts --initial
    $ python manage.py migrate accounts



Production/Staging
-------------------
In production/staging things are very similar.
The only difference is that we use virtualenv instead of virtualenvwrapper, so the step #2 is different.

### 2. Create a virtual environment
In production we use plain virtualenv.

    $ virtualenv ve
Or:

    $ virtualenv ve -p /usr/bin/python2.7

Next set the right settings file and passwords as environment variables.
We also set a 50 chars SECRET_KEY.
Virtualenv hook on activation:

    $ nano ve/bin/activate
    export DJANGO_SETTINGS_MODULE=icecreamshop.settings.local
    export SECRET_KEY='h65fsd^&%khfg%$#(*&hgfHJFGhJKghhjJK7&*8fHGF^%^&567'
    export MY_SECRET="my_secret_password"

There is no a hook on deactivation so we won't unset those environment vars; this is not an issue.

Activate the virtual environment:

    $ source ve/bin/activate
