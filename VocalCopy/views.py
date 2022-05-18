import os
from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage

#python scripts
from VocalCopy.backend import fft
from .backend.fft import fastFourierTransform

def index(request):
    # TestFunction()
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        fastFourierTransform(f'media/{uploaded_file.name}')
        os.remove(f'media/{uploaded_file.name}')
    return render(request, "index.html")
