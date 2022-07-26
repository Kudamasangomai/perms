from django.urls import path
from .models import *
from django_downloadview import ObjectDownloadView
from . import views
from .views import (

	FarmlistView



	 )

download = ObjectDownloadView.as_view(model=documents, file_field=
'coi')

urlpatterns = [    

  
   path('register_farmer/',views.register_farmer, name ='register-farmer'),
   path('farms/<int:pk>',FarmlistView.as_view(),name="farms-list"),
   path('documents/',views.add_documents,name="add-documents"),
   path('download/', download, name="default"),


  
 
  
]

