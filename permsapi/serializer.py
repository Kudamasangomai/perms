from rest_framework import serializers
from farmers.models import *
from applications.models import *
from users.models import *
from django.contrib.auth.models import User


class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = application
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','is_staff','is_active']



class FarmsSerializers(serializers.ModelSerializer):
    class Meta:
        model = farm
        fields ='__all__'

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields ='__all__'