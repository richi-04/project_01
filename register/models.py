from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# hobby = [('dance','Dance'), ('travel','Travelling'), ('reading','Reading'), ('art','Art')]
gender = [('male','Male'), ('female', 'Female')]

class Profile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=gender)
    password = models.CharField(max_length=255)
    hobby = models.CharField(max_length=255)

    def __str__(self):
        return self.name
