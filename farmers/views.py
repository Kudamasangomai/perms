from multiprocessing import context
from urllib import request
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from main.forms import *
from .models import *

# Create your views here.
class FarmlistView(ListView):
    model = farmer
    template_name = 'farmers/farms-list.html' 
    paginate_b = 10   

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['farms'] = farmer.objects.filter(fuser = self.request.user)
        return ctx

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
            return redirect('farms-list',profile.id)
    else:
        registerfarmerform = RegisterFarmerForm()
    return render(request,'farmers/register-farmer.html',{'registerfarmerform': registerfarmerform})



def add_documents(request):
    # protocol = 'http://'	
    # host = request.get_host()
    # link = protocol + host + reverse('book-detail',kwargs={'pk':b.bookid_id})
    
    profile = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        documentsform = DocumentForm(request.POST,request.FILES)
        if documentsform.is_valid():
            farmer = documentsform.save(commit=False)      
            farmer.fuserd = request.user
            print(farmer)
            farmer.save()
            #messages.success(request, f'Documents successfully added')
            return redirect('farms-list',profile.id)
    else:
        data={
              'documentsform' : DocumentForm(),
              'documentsavail': documents.objects.get(fuserd =request.user)
        }
      
    return render(request,'farmers/add_documents.html',data)










