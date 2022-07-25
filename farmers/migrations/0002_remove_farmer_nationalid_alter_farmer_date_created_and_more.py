# Generated by Django 4.0.6 on 2022-07-25 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='nationalid',
        ),
        migrations.AlterField(
            model_name='farmer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='farm_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]