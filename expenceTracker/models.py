from django.db import models


# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)