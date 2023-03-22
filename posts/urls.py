from django.urls import path
from .views import posts_list, post_details, authors_list, author_details


app_name='posts'
urlpatterns = [
   

   path('posts/list', posts_list, name='posts_list'),
   path('posts/details/<int:id>', post_details, name='post_details'),
   path('authors/list', authors_list, name='authors_list'),
   path('authors/details/<int:id>', author_details, name='author_details'),
]