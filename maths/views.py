
# maths/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from maths.forms import ResultForm
from maths.models import Math, Result
# Create your views here.

def math(request):
   return HttpResponse("Tu będzie matma")




def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='add', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )

def sub(request, a, b):  
   a, b = int(a), int(b)
   wynik = a-b
   c = {"a":a, "b":b, "operacja": "-" ,"wynik":wynik}

   result = Result.objects.get_or_create(value=wynik)[0]
   Math.objects.create(operation='sub', a=a, b=b, result=result)
   return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
   )



def mul(request, a, b):
   a, b = int(a), int(b)
   wynik = a*b
   c = {"a":a, "b":b, "operacja": "*" ,"wynik":wynik}

   result = Result.objects.get_or_create(value=wynik)[0]
   Math.objects.create(operation='mul', a=a, b=b, result=result)
   return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
   )

def div(request, a, b):
   a, b = int(a), int(b)
   if b == 0:
       return HttpResponse("Nie dziel przez 0")
   wynik = a/b
   c = {"a":a, "b":b, "operacja": "/" ,"wynik":wynik}
   result = Result.objects.get_or_create(value=wynik)[0]
   Math.objects.create(operation='div', a=a, b=b, result=result)
   return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
   )

@login_required
def maths_list(request):
   maths = Math.objects.all()
   math_model_names = Math._meta.get_fields()
   paginator = Paginator(maths, 5)
   page_number = request.GET.get('page')
   maths = paginator.get_page(page_number)
   return render(
       request=request,
       template_name="maths/list.html",
       context={"maths": maths, "math_model_names": math_model_names}
   )

def math_details(request, id):
   math = Math.objects.get(id=id)
   return render(
       request=request,
       template_name="maths/details.html",
       context={"math": math}
   )

def results_list(request):
   if request.method == "POST":
       form = ResultForm(data=request.POST)

       if form.is_valid():
           if form.cleaned_data['error'] == '':
               form.cleaned_data['error'] = None
           Result.objects.get_or_create(form.cleaned_data)
           messages.add_message(
               request,
               messages.SUCCESS,
               "Utworzono nowy Result!!"
           )
       else:
           messages.add_message(
               request,
               messages.ERROR,
               form.errors['__all__']
           )

   form = ResultForm()
   results = Result.objects.all()
   return render(
       request=request,
       template_name="maths/results.html",
       context={
           "results": results,
           "form": form
       }
   )