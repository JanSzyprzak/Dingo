# maths/admin.py
from django.contrib import admin
from posts.models import Post, Author

# Register your models here.




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'email', 'bio']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "created", "modified", 'author']
    list_filter = ["author"]
    search_fields = ["title", "content"]





