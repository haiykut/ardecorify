# example/urls.py
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from example.views import index,login,register,logout_request


urlpatterns = [
    path('', index,name='index'),
    path('login', login,name='login'),
    path('register', register,name='register'),
    path("logout",logout_request, name="logout"),
]
urlpatterns += staticfiles_urlpatterns()
