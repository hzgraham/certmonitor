import urllib, bs4, urllib.request, csv, os, xmlrpc.client, xmlrpc.server
from xmlrpc import client, server
from time import sleep

from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from dashboard.utils import handle_uploaded_file

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Home(request):
    # /certmonitor/ url
    template = 'dashboard/base.html'
    # context = {'encouragement': encouragement()}
    context = []
    return render(request, template, context)

# def upload_file(request):
#     if request.method == 'GET':
#         form = UploadFileForm(request.GET, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/dashboard/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'dashboard/base.html', {'form': form})

