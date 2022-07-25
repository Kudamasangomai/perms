from django.urls import path
from . import views



urlpatterns = [    

  
   path('register_farmer/',views.register_farmer, name ='register-farmer'),


  
 
  
]

