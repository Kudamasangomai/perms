from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator,MinValueValidator
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime ,timedelta


class farmer(models.Model):
    farming_type_choices =(
        ("Subsistence","Subsistence "),
        ("Commercial","Commercial"),
    
    )
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    fuser = models.ForeignKey(User,on_delete = models.CASCADE)
    farm_name = models.CharField(max_length=50,unique=True)
    farm_address = models.CharField(max_length=100)
    farming_type = models.CharField(max_length=20,choices =farming_type_choices)
    farm_size = models.IntegerField(validators =[MinValueValidator(0)])
    date_created = models.DateTimeField(default=datetime.today)


    def __str__(self):
        return self.farm_name

class documents(models.Model):
    fuserd = models.OneToOneField(User,on_delete = models.CASCADE)
    coi = models.FileField(upload_to='documents',default='N/A')
    cr = models.FileField(upload_to='documents',default='N/A')
    tax_clearence = models.FileField(upload_to='documents',default='N/A')


    def __str__(self):
        return f'{self.fuserd.username} Documents '
    
