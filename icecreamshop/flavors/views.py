from django.shortcuts import render


def home(request, template='home.html'):
    args = {}
    return render(request, template, args)
