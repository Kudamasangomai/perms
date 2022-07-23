from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    a = User.objects.get(id = request.user.id)
    if a.profile.role < 3:
        return render(request, 'main/fdashboard.html')
    return render(request, 'main/dashboard.html')