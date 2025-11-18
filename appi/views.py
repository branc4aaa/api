from django.shortcuts import render, redirect

from appi.forms import RegistrationForm , Postform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from appi.models import Posts

def homeView(request):
    return render(request, 'index.html')

def singupView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            nuevo = User(username=username, email=form.cleaned_data.get('email'), first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'))
            nuevo.set_password(form.cleaned_data.get('password1'))
            nuevo.save()
            return render(request, "message.html", {'message': f'User {username} registered successfully'})
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
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def postsView(request):
    return render(request, 'posts.html', {'posts': Posts.objects.all()})

@login_required
def addPost(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = form.cleaned_data.get('author')
            new_post = Posts(title=title, body=content, author=author)
            new_post.save()
            return redirect('posts')
        else:
            return render(request, "message.html", {'message': 'Post creation failed'})
    form = Postform()
    return render(request, 'post.html', {'form': form})