from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetings(request, name = ""):
    if name == "":
        return HttpResponse("Hello World!")
    return HttpResponse(f"Hello {name.capitalize()}!")

def home(request):
    return render(
        request=request,
        template_name="greetings/index.html"
    )

def about(request):
    return render(
        request=request,
        template_name="greetings/about.html"

    )

def contact(request):
    return render(
        request=request,
        template_name="greetings/contact.html"

    )