from django.shortcuts import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse("Hello World!")

def welcome(request):
    return HttpResponse("Welcome!")