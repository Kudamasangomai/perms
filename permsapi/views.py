from django import views
from django.shortcuts import render
from applications.models import *
from rest_framework import viewsets
from .serializer import *
from django.contrib.auth.models import User

# Create your views here.
class ApplicationView(viewsets.ModelViewSet):
    queryset = application.objects.all()
    serializer_class = ApplicationSerializers

class UserView(viewsets.ModelViewSet):
    #queryset = User.objects.filter(is_staff = False)
    queryset = User.objects.all()
    serializer_class = UserSerializers

class Farmview(viewsets.ModelViewSet):
    queryset = farm.objects.all()
    serializer_class = FarmsSerializers

class Profileview(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializers


