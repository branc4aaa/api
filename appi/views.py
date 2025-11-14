from django.shortcuts import render
from django.http import JsonResponse
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
            return JsonResponse({'message': 'User registered successfully'})
        else:
            return JsonResponse({'message': 'Registration failed'})
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
                return JsonResponse({'message': f'Welcome {username}'})
            else:
                return JsonResponse({'message': 'Invalid credentials'})
        else:
            return JsonResponse({'message': 'Invalid credentials'})
        
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})