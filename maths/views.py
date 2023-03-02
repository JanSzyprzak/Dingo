
# maths/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def math(request):
   return HttpResponse("Tu będzie matma")

def add(request, a, b):
   a, b = int(a), int(b)
   return HttpResponse(a + b)

def sub(request, a, b):
   a, b = int(a), int(b)
   return HttpResponse(a - b)

def mul(request, a, b):
   a, b = int(a), int(b)
   return HttpResponse(a * b)

def div(request, a, b):
   a, b = int(a), int(b)
   if b == 0:
       return HttpResponse("Nie dziel przez 0")
   return HttpResponse(a / b)