from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import Q ,Count
from django.db.models.functions import TruncMonth
from farmers.models import *
from django.contrib.auth.decorators import login_required

from applications.models import application

# Create your views here.
@login_required
def dashboard(request):
    a = User.objects.get(id = request.user.id)
    if a.profile.role  == 2:
        return redirect('applications')
    if a.profile.role < 3:
        context ={
        'user_permits':application.objects.filter(user = request.user).count(),
        'user_processing_permits':application.objects.filter(user = request.user,status='Processing').count(),
        'user_Approved_permits':application.objects.filter(user = request.user,status='Approved').count(),
        'user_Notapproved_permits':application.objects.filter(user = request.user,status='NotApproved').count(),
        'user_unpaid_permits':application.objects.filter(user = request.user,status='Approved',permit_paid='false').count(),
        'total_farms': farm.objects.filter(fuser =request.user).count(),
        'a' : a
        }
        return render(request, 'main/dashboard.html',context)
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