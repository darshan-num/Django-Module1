from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=50,default=None)
    phone = models.CharField(max_length=10,default=None)
    role = models.CharField(max_length=32,default=None)

