from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def hello_world(request):
    return HttpResponse("Hello World")