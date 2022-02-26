from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.username} signed up'

class LogIn(models.Model):
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=16)
    
    def __str__(self):
        return f'{self.username} loged in'