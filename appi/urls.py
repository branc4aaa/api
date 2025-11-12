from django.urls import path
from appi.views import homeView

urlpatterns = [
    path('', homeView, name='index'),
]
