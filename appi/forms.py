from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appi.models import Posts as Post

class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']