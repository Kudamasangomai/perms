import random
from ssl import Purpose
from django.db import models
from datetime import datetime ,timedelta
from django.contrib.auth.models import User


def randpermitno():
    return str(random.randint(1001,999999))


# Create your models here.
class application(models.Model):
    permit_choices=(
        ("Import","Import "),
        ("Export","Export"),
       
    )
    portOfEntryExitChoices =(
        ('HarareAirport','HarareAirport'),
        ('BulawayoAirport','BulawayoAirport'),
        ('HarareRailwayStation','HarareRailwayStation'),
        ('BeitBridgeBorderPost','BeitBridgeBorderPost'),
        ('ChirunduBorderPost','ChirunduBorderPost'),
        ('NyamapandaBorderPost','NyamapandaBorderPost')  ,     
        
    )
    purporsechoices =(
        ('sale','sale'),
        ('privateuse','privateuse'),
        ('Consumption','Consumption'),
        ('Medicinal','Medicinal'),
    )
    statuschoice=(
        ('waiting','Waiting'),
        ('Processing','Processing'),
        ('Approved','Approved'),
        ('NotApproved','NotApproved'),
        
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    permit_number = models.CharField(max_length=20,default=randpermitno,unique=True)
    permit_type = models.CharField(max_length=50,choices = permit_choices)  
    product_name = models.CharField(max_length=50)
    port_of_entry_exit =models.CharField(max_length=50,choices=portOfEntryExitChoices)
    status = models.CharField(max_length=50,choices=statuschoice,default='waiting')
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    Purpose = models.CharField(max_length=20,choices=purporsechoices)
    date_created = models.DateTimeField(default=datetime.today) 
    Approving_officer = models.ForeignKey(User,default=0,on_delete=models.CASCADE, db_constraint=False,related_name='Approving_officer')
    date_approved = models.DateTimeField(default=datetime.today) 
    StatusReason = models.CharField(max_length=100,default='waitingstatus')


    def __str__(self):
        return self.permit_number
    