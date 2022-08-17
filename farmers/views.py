from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,UpdateView
from django.contrib import messages
from django.db.models import Q ,Count
from users.models import *
from farmers.models import *
from main.forms import *
from .models import *
from django.http import HttpResponse
import csv

#all below import are for generating a pdf 
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import FileResponse, HttpResponse

# Create your views here.
class farmers(LoginRequiredMixin,ListView):
    model = User
    template_name = 'farmers/farmers.html'
    paginate_by = 10

    def get_context_data(self,**kwargs):
       context = super(farmers, self).get_context_data(**kwargs)
       context['farm_count'] = farm.objects.values('fuser_id').annotate(count=Count('fuser_id'))
       context['farmers'] = User.objects.filter(is_staff = False)
       return context


class FarmlistView(LoginRequiredMixin, ListView):
    model = farm
    template_name = 'farmers/farms-list.html' 
    paginate_by = 10   

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.profile.role > 4:
            ctx['farms'] = farm.objects.all()
        else:
            ctx['farms'] = farm.objects.filter(fuser = self.request.user)
        return ctx
  

#function to add User farm details
@login_required
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
@login_required
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
    
@login_required
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

@login_required      
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

#search function
@login_required
def search_farm(request):

	if request.method == 'POST':
		searchedq = request.POST.get('user_search_input')	
			
						
		farms = farm.objects.filter(Q(fuser = request.user),
			Q(farm_name__contains = searchedq) |
			Q(farm_district__contains = searchedq) |
			Q(fuser__first_name__contains = searchedq) |
			Q(fuser__last_name__contains = searchedq)
			)
		return render(request,'farmers/farms-list.html',{'farms':farms})
	else:
		return render(request,'farmers/farms-list.html')

#search function
@login_required
def search_farmer(request):

	if request.method == 'POST':
		searchedq = request.POST.get('user_search_input')	
			
						
		farmers = User.objects.filter(
					Q(first_name__contains = searchedq)
			)
		return render(request,'farmers/farmers.html',{'farmers':farmers})
	else:
		return render(request,'farmers/farmers.html')


@login_required
def export_farmers_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    # c.drawString(100, 100, "Let's generate this pdf file.")
    textob = c.beginText()
	
    textob.setFont("Helvetica",14)
    objbooks = User.objects.filter(is_staff = False)
    row = (['Name','Last Name','email'])
    for objb in objbooks:
        
        row.append( objb.first_name)
        row.append(objb.last_name)
        row.append(objb.email)

    for line in row:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Farmerslist.pdf')


    
@login_required
def export_farmers_csv(request):
    
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']=  'attachment; filename=farmers.csv'
	writer =csv.writer(response)
	writer.writerow(['Name','Last Name','email'])
	objbooks = User.objects.filter(is_staff = False)

	for objb in objbooks:
		writer.writerow([
            objb.first_name,
            objb.last_name ,    
            objb.email,          
           
                  
            ]),
	return response

 







