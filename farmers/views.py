from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,UpdateView
from django.contrib import messages
from multiprocessing import context
from urllib import request
from users.models import *
from farmers.models import *
from main.forms import *
from .models import *


# Create your views here.
class farmers(LoginRequiredMixin,ListView):
    model = User
    template_name = 'farmers/farmers.html'
    context_object_name  = 'farmers'
    paginate_by = 10


class FarmlistView(ListView):
    model = farm
    template_name = 'farmers/farms-list.html' 
    paginate_b = 10   

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['farms'] = farm.objects.filter(fuser = self.request.user)
        return ctx


#function to add User farm details
def register_farm(request):
    profile = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        registerfarmform = RegisterFarmForm(request.POST)
        if registerfarmform.is_valid():
            farmer = registerfarmform.save(commit=False)      
            farmer.fuser = request.user
            farmer.save()
            messages.success(request, f'Your Farm has successfully  been Registered')
            return redirect('farms-list',profile.id)
    else:
        registerfarmform = RegisterFarmForm()
    return render(request,'farmers/register-farm.html',{'registerfarmerform': registerfarmform})

#function to updated User farm details
def UpdateFarmView(request,pk):
    profile = get_object_or_404(User, id=request.user.id)    
    if request.method == 'POST':
        form = RegisterFarmForm(request.POST ,instance =  farm.objects.get(id = pk))       
        if form.is_valid():
            form.save()	
            messages.success(request, f'Your Farm details has successfully  been Updated')
            return redirect('farms-list',profile.id)		
    else:   
        registerfarmform = RegisterFarmForm( instance =  farm.objects.get(id =pk))
    return render(request,'farmers/farm-edit.html',{'registerfarmerform': registerfarmform})    
    

def add_documents(request):    
    profile = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        documentsform = DocumentForm(request.POST,request.FILES)
        if documentsform.is_valid():
            farmer = documentsform.save(commit=False)      
            farmer.fuserd = request.user
            print(farmer)
            farmer.save()
            messages.success(request, f'Documents successfully added')
            return redirect('farms-list',profile.id)
    else:
        data={
              'documentsform' : DocumentForm(),
              'documentsavail': documents.objects.filter(fuserd =request.user)
        }
      
    return render(request,'farmers/add_documents.html',data)

        
def edit_documents(request,**kwargs):
    profile = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        documentsform = DocumentForm(request.POST,request.FILES, instance = request.user.documents)
        if documentsform.is_valid():           
            documentsform.save()
            messages.success(request, f'Documents successfully Updated')
            return redirect('farms-list',profile.id)
    else:
        documentsform = DocumentForm( instance = request.user.documents)
        data={

              'documentsform' : documentsform
        }
      
    return render(request,'farmers/edit_documents.html',data)








