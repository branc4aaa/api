from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Postform(forms.Form):

    title = forms.CharField(max_length=50)
    title2 = forms.CharField(max_length=30)
    content = forms.CharField(max_length=10000)
    author = forms.CharField(max_length=30)

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]