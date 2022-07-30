from django.urls import path
from .models import *
from django_downloadview import ObjectDownloadView
from . import views
from .views import (

	FarmlistView,
   farmers,

   

	 )

download = ObjectDownloadView.as_view(model=documents, file_field='coi')

urlpatterns = [    

  
   path('register_farm/',views.register_farm, name ='register-farm'),
   path('farms/<int:pk>',FarmlistView.as_view(),name="farms-list"),
   path('update_farm/<int:pk>',views.UpdateFarmView,name="update-farm"), 
   path('documents/',views.add_documents,name="add-documents"),
   path('edit_documents/<fuserd_id>',views.edit_documents,name="edit-documents"),
   path('download/', download, name="default"),
   path('farmers',farmers.as_view(),name='farmers')

  
 
  
]

