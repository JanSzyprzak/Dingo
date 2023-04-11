from django.urls import path
from .views import greetings, home, about, contact

app_name="greetings"

urlpatterns = [
   path('greetings/', greetings),
   path('greetings/<name>/', greetings),
   path('', home, name="home"),
   path('about', about, name="about"),
   path('contact', contact, name="contact")
]