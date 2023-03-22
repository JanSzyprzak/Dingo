from django import forms
from .models import Author

authors_choicelist = [(a.nick, a.nick) for a in Author.objects.all()]

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField(choices = authors_choicelist)


class AuthorForm(forms.Form):
    nick = forms.CharField()
    email = forms.EmailField()
    bio = forms.CharField(required=False, widget=forms.Textarea)
    