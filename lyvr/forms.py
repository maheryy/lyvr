from django import forms

from .models import BookExample

class BookExampleForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    description = forms.CharField(label='Description', max_length=100)

    class Meta:
        model = BookExample
        fields = ['title', 'author', 'description']