from django.db import models

# Create your models here.





class Author(models.Model):
   nick = models.CharField(max_length=30)
   email = models.EmailField(default='author@example.com')
   bio = models.TextField(blank=True)



class Post(models.Model):
   title = models.CharField(max_length=30)
   content = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   author = models.ForeignKey('posts.Author',
                                 on_delete=models.CASCADE,
                                 null=False,
                                 blank=False
                                 )
   