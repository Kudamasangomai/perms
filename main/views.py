from django.shortcuts import render
from django.contrib.auth.models import User

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
        'total_processing_permits' : application.objects.filter(status = 'processing').count()
    }
    return render(request, 'main/dashboard.html',context)