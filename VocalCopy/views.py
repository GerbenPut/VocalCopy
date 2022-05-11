from django.shortcuts import render
from django.http import HttpResponse

#python scripts
from VocalCopy.backend import test
from .backend.test import TestFunction


def index(request):
    TestFunction()
    return render(request, "index.html")
