"""Development settings and globals."""

from os.path import join, normpath
from os import environ

# Extend base settings
from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(BASE_DIR, 'moogle.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## SECRET KEY
# Secret key is an environment variable in production
SECRET_KEY = environ['SECRET_KEY']
########## END SECRET KEY