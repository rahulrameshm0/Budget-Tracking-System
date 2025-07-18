from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

class Transactions(models.Model):
    TRANSACTION_TYPES = (('Income','Income'),
                        ('Expense','Expense')
                        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, default='untitle')
    category = models.CharField(max_length=150)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(max_length=150, default='No description')
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='Expense')