# Stdlib imports
# E.g.: from math import sqrt

# Core Django imports
from django.shortcuts import render

# Third-party app imports
# E.g.: from django_extensions.db.models import TimeStampedModel

# Imports from local apps
# E.g.: from .models import BananaSplit


def home(request, template='home.html'):
    args = {}
    return render(request, template, args)
