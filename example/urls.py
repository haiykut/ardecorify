# example/urls.py
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from example.views import index,login,logout_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index,name='index'),
    path('login', login,name='login'),
    path("logout",logout_request, name="logout"),
]
urlpatterns += staticfiles_urlpatterns()