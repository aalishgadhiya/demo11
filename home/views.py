from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, This Is Home Page!!!%")


def about_us(request):
    return HttpResponse("Hello, This Is About Us")


def contect_us(request):
    return HttpResponse("Hello, This Is Contect Us")