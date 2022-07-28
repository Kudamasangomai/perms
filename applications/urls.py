from django.urls import path
from .models import *
from . import views
from .views import (ApplicationsliStView )



urlpatterns = [    

  
   path('',ApplicationsliStView.as_view(),name="Application")


  
 
  
]

