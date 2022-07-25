from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from main.forms import *

# Create your views here.

def register_farmer(request):
    profile = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        registerfarmerform = RegisterFarmerForm(request.POST)
        if registerfarmerform.is_valid():
            farmer = registerfarmerform.save(commit=False)      
            farmer.fuser = request.user
            farmer.save()
            messages.success(request, f'Record successfully added')
            print(profile)
            return redirect('user-profile',profile.id)
    else:
        registerfarmerform = RegisterFarmerForm()
    return render(request,'farmers/register-farmer.html',{'registerfarmerform': registerfarmerform})



