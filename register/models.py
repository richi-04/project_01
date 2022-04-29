from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser




# Create your models here.


gender = [('male','Male'), ('female', 'Female')]

class Profile(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    hobby = models.CharField(max_length=255)

    def __str__(self):
        return self.username
