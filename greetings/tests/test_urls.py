from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from greetings.views import greetings

class TestUrls(TestCase):

    def test_resolution_for_greetings(self):
        resolver=resolve('/greetings/')
        self.assertEqual(resolver.func, greetings)
    
   

    
           