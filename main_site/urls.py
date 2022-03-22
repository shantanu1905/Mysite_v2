from django.contrib import admin
from django.urls import path 
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,  index , name="home"),
    path('contact', contact , name="contact"),
    path('signup',handleSignup , name="signup" ),
    path('login',  handleLogin , name="login"),
    path('logout', handleLogout , name="logout" ),
    path('dashboard',dashboard , name="dashboard") ,
    path('writes', writes , name="writes"),
]