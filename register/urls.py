from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerForm),
    path('login', views.loginForm),
    path('home', views.home)
]