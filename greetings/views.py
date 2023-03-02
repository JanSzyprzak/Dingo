from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetings(request, name = ""):
    if name == "":
        return HttpResponse("Hello World!")
    return HttpResponse(f"Hello {name.capitalize()}!")
