from django.test import TestCase
from posts.models import Post, Author

class MathModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="testowy", content='nic', author=Author.objects.create(nick='test', email='test@test.com', bio ='test'))
        Post.objects.create(title="testowy2", content='nic2', author=Author.objects.create(nick='test2', email='test2@test.com', bio ='test2'))


    def test_post_str(self):
        p1 = Post.objects.get(title="testowy")
        p2 = Post.objects.get(title="testowy2")

        self.assertEqual(str(p1), 'Post object (1)')
        self.assertEqual(str(p2), 'Post object (2)')


    def test_author_str(self):
        a1 = Author.objects.create(nick='test', email='test@test.com', bio ='test')
        a2 = Author.objects.create(nick='test2', email='test2@test.com', bio ='test2')

        self.assertEqual(str(a1), 'test')
        self.assertEqual(str(a2), 'test2')
                                   



