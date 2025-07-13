from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    amount = models.FloatField()
    date = models.DateField()