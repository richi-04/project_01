from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerForm, name='register'),
    path('login', views.loginForm, name='login'),
    path('home', views.home, name='home')
]