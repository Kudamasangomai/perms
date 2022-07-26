# Generated by Django 4.0.6 on 2022-07-29 19:41

import applications.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Approving_officer',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Approving_officer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='StatusReason',
            field=models.CharField(default='waiting', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='permit_number',
            field=models.CharField(default=applications.models.randpermitno, max_length=20, unique=True),
        ),
    ]
