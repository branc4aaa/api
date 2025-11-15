from django.urls import path
from appi.views import homeView, singupView, loginView, profileView, postsView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', homeView, name='index'),
    path('singup/', singupView, name='singup'),
    path('login/', loginView, name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('profile/', profileView, name='profile'),
    path('posts/', postsView, name='posts'),
]
