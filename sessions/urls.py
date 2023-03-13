# sessions/urls.py
from django.urls import path

from sessions import views

urlpatterns = [

   path('set', views.set_session),
   path('get', views.get_session)
]