from django.urls import path
from appi.views import homeView, singupView, loginView

urlpatterns = [
    path('', homeView, name='index'),
    path('signup/', singupView, name='signup'),
    path('login/', loginView, name='login'),
]
