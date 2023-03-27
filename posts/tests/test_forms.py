from django.test import TestCase
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

class PostFormTest(TestCase):

    def test_post_save_correct_data(self):
        data = {"title": 'test', 'content': 'cos', 'author': Author.objects.create(nick='test', email='test@test', bio='test')}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Post)
        self.assertEqual(r.title, 'test')
        self.assertIsNotNone(r.id)

    def test_author_save_correct_data(self):
        data = {"nick": 'test', 'email': 'cos@cos.com', 'bio': 'cos'}
        self.assertEqual(len(Author.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Author)
        self.assertEqual(r.nick, 'test')
        self.assertIsNotNone(r.id)
        
