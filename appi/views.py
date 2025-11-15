from django.shortcuts import render, redirect

from appi.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


def homeView(request):
    return render(request, 'index.html')

def singupView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            nuevo = User(username=username)
            nuevo.set_password(form.cleaned_data.get('password1'))
            nuevo.save()
            return redirect('index')
        else:
            return render(request, "message.html", {'message': 'Registration failed'})
    form = RegistrationForm()
    return render(request, 'singup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':       
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "message.html",{'message': f'Welcome {username}'})
            else:
                return render(request, "message.html",{'message': 'Invalid credentials'})
        else:
            return render(request, "message.html",{'message': 'Invalid credentials'})
        
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required
def profileView(request):
    return render(request, 'profile.html')

@login_required
def postsView(request):
    return render(request, 'posts.html')