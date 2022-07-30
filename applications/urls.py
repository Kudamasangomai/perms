from unicodedata import name
from django.urls import path
from .models import *
from . import views
from .views import (ApplicationsliStView,ApplyPermitView )



urlpatterns = [    

  
   path('',ApplicationsliStView.as_view(),name="applications"),
   path('apply_permit',ApplyPermitView.as_view(),name="apply-permit"),
   path('assign_officer/<int:pk>',views.assign_officer,name="assign-officer")


  
 
  
]

