from django import forms
from .models import Author, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
    
