# Generated by Django 5.2.4 on 2025-07-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenceTracker', '0002_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='description',
            field=models.TextField(default='no description', max_length=150),
        ),
    ]
