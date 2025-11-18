from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Postform(forms.Form):

    title = forms.CharField(max_length=50)
    title2 = forms.CharField(max_length=30)
    content = forms.CharField(max_length=10000)
    author = forms.CharField(max_length=30)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']