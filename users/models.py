from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator,MinValueValidator


class profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image =  models.ImageField(default='default.jpg' ,upload_to = 'profile_pics')
    user_phone =  models.IntegerField(default=0)
    role = models.IntegerField(default=0)
    nationalid = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.user.username


