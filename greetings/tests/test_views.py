from django.test import TestCase, Client




class GreetingsViewsTest(TestCase):

    def setUp(self):
        
        self.client = Client()

    def test_greetings(self):
        response = self.client.get("/greetings", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello World!', response.content.decode())

    def test_personalized_greetings(self):
        response = self.client.get("/greetings/jan", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello Jan!', response.content.decode())
        