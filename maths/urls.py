# maths/urls.py
from django.urls import path
from .views import math, add, sub, mul, div

urlpatterns = [
   path('maths/', math),
   path('maths/add/<int:a>/<b>', add),
   path('maths/sub/<int:a>/<b>', sub),
   path('maths/mul/<int:a>/<b>', mul),
   path('maths/div/<int:a>/<b>', div),
]