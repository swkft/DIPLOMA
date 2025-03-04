from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
    with open(os.path.join('myapp/static/html/index.html'), 'r') as f:
        return HttpResponse(f.read())
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')



def log_in(request):
    return render(request, 'log_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def blog(request):
    return render(request, "blog.html")


def for_therapist(request):
    return render(request, "for_therapist.html")


def help_center(request):
    return render(request, "help_center.html")