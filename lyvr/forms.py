from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import BookExample, User


class BookExampleForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    description = forms.CharField(label='Description', max_length=100)

    class Meta:
        model = BookExample
        fields = ['title', 'author', 'description']


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['email'].label = "Adresse email"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterProForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterProForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['email'].label = "Adresse email"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
