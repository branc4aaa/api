from django.urls import path
from appi.views import homeView, singupView, loginView, profileView, postsView, addPost
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homeView, name='index'),
    path('singup/', singupView, name='singup'),
    path('login/', loginView, name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('profile/', profileView, name='profile'),
    path('posts/', postsView, name='posts'),
    path('addpost/', addPost, name='addPost'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)