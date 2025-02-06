from django.http import HttpResponse

def index(request):
    return HttpResponse("Вітаємо на сторінці index!")
