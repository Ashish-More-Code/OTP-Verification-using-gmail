from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *
 
# Create your models here.
class myuser(AbstractUser):
    username=None
    otp=models.IntegerField(default=0)
    phone_number = models.CharField(max_length=12, unique=True)
    USERNAME_FIELD = 'phone_number'

    objects=CustomUserManager()