from django.test import TestCase, Client
from posts.models import Post, Author



class MathViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(title="tytuł", content="zawartość", author=Author.objects.create(nick='testowy', email="jakis@exapmle.com", bio='cos o autorze'))
        Author.objects.create(nick='testowy', email='cos@cos', bio='cos')
        self.client = Client()

    def test_posts_list(self):
        response = self.client.get("/posts/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts_list"]), 1)
        self.assertIn('<li><a href="/posts/details/1">tytuł</a></li>', response.content.decode())

    def test_authors_list(self):
        response = self.client.get("/authors/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["authors_list"]), 2)
        self.assertIn('<li><a href="/authors/details/1">testowy</a></li>', response.content.decode())
        