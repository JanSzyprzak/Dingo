from django.test import TestCase, Client
from maths.models import Math, Result



class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        Result.objects.create(value='1')
        self.client = Client()

    def test_maths_list(self):
        response = self.client.get("/maths/histories", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>', response.content.decode())

    def test_results_list(self):
        response = self.client.get("/maths/results", follow=True)
        self.assertEqual(len(response.context["results"]), 1)
        self.assertIn('<li>value: 1.0 | error: None</li>', response.content.decode())
        


        