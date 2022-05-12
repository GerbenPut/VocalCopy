from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage

#python scripts
from VocalCopy.backend import test
from .backend.test import TestFunction

def index(request):
    # TestFunction()
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, "index.html")
