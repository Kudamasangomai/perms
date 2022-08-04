from unicodedata import name
from django.urls import path
from .models import *
from . import views
from .views import (ApplicationsliStView,ApplyPermitView,ApplicantView,ApplicationUpdateView )



urlpatterns = [    

  
   path('',ApplicationsliStView.as_view(),name="applications"),
   path('apply_permit',ApplyPermitView.as_view(),name="apply-permit"),
   path('assign_officer/<int:pk>',views.assign_officer,name="assign-officer"),
   path('approve_permit/<int:pk>',views.approve_permit,name="approve-permit"),
   path('reject_permit/<int:pk>',views.reject_permit,name="reject-permit"),
   path('applicant_details/<int:pk>',ApplicantView.as_view(),name="applicant-details"),
   path('application_aupdate/<int:pk>',ApplicationUpdateView.as_view(),name='application-update'),
   path('payment/<int:pk>',views.payment,name="payment"),
   path('process_payment/<int:pk>',views.process_payment,name='process-payment'),

   # path('export_csv/',views.export_csv,name="export-csv"),
   path('export_pdf/<int:pk>',views.export_pdf,name="export-pdf"),
  
 
  
]

