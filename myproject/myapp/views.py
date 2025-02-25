from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
    with open(os.path.join('myapp/static/html/index.html'), 'r') as f:
        return HttpResponse(f.read())
def index(request):
    return render(request, 'index.html')