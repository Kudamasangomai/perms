from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q ,Count
from django.db.models.functions import TruncMonth

from applications.models import application

# Create your views here.
def dashboard(request):
    a = User.objects.get(id = request.user.id)
    if a.profile.role < 3:
        return render(request, 'main/fdashboard.html')
    context={
        'total_farmers' : User.objects.filter(is_staff = False).count(),
        'total_users' : User.objects.filter(is_staff = True).count(),
        'total_waiting_permits' : application.objects.filter(status = 'waiting').count(),
        'total_processing_permits' : application.objects.filter(status = 'Processing').count(),
        'approved': application.objects.filter(status='Approved').annotate(month=TruncMonth('date_approved')).values('month').annotate(c=Count('id')).values('month', 'c'),
        'd': application.objects.annotate(month=TruncMonth('date_created')).values('month').annotate(c=Count('id')).values('month', 'c'), 
        'rejected': application.objects.filter(status='NotApproved').annotate(month=TruncMonth('date_created')).values('month').annotate(c=Count('id')).values('month', 'c'),
    
       }
    return render(request, 'main/dashboard.html',context)