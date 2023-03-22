# maths/urls.py
from django.urls import path
from .views import math, add, sub, mul, div, maths_list, math_details, results_list



app_name="maths"
urlpatterns = [
   path('maths/', math),
   path('maths/add/<int:a>/<b>', add),
   path('maths/sub/<int:a>/<b>', sub),
   path('maths/mul/<int:a>/<b>', mul),
   path('maths/div/<int:a>/<b>', div),
   path('maths/histories/', maths_list, name="list"),
   path('maths/histories/<int:id>', math_details, name="details"),
   path('maths/results/', results_list, name="results"),
]