from .models import *
from farmers.models import *
from main.forms import *
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView ,UpdateView,DeleteView,FormView,DetailView,CreateView


#list all application of the Logged in User but admin user an view All
class ApplicationsliStView(LoginRequiredMixin, ListView):
    model = application
    template_name = 'applications/applications-list.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationsliStView,self).get_context_data(**kwargs)
        
        if self.request.user.is_superuser:
             context['applications'] = application.objects.all()
        else:
            context['user_has_farm'] = farm.objects.filter(fuser = self.request.user)
            context['applications'] = application.objects.filter(user = self.request.user)
        return context



class ApplyPermitView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = application
    form_class = PermitApplicationForm
    template_name = 'applications/application-form.html' 
    success_message = " Permit Succesfully Submitted"  
    success_url = reverse_lazy('applications')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ApplicantView(DetailView):
    model = application
    template_name = 'applications/applicant_verification.html'

    # def get_context_data(self,**kwargs):
    #     context = super(ApplicantView,self).get_context_data(**kwargs)
    #     #context['userdocs'] = documents.objects.filter(fuserd_id = self.kwargs['pk'])


def assign_officer(request,pk):
    

    app = application.objects.get(id=pk)
    appwoner = User.objects.get(id=app.user_id)
    appofficerid = request.POST.get('officerid')
    
    if request.method == 'POST':
        user = User.objects.get(id=appofficerid )
        app.Approving_officer = user
        app.status = 'Processing'
        app.save()
        subject = "New Notification - Perms"
     
        message = " Your application in Now being proccesed "
        recipient_list = [appwoner.email,]
        send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently = False)
        messages.success(request,f' Application succefully Assigned')
        return redirect('applications')
    
    else:
        context={
            'officer' : User.objects.all(),
             'application' : application.objects.get(id=pk)
        }       
        return render(request,'applications/assign-form.html',context)



def approve_permit(request,pk):
    app = application.objects.get(id=pk)
    if request.method == 'POST':
        
        app.status = 'Approved'
        app.StatusReason =  'Approved'
        app.save()
        # subject = "New Notification - Perms"     
        # message = " Your application Has been Approved "
        # recipient_list = [app.user.email,]
        # send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently = False)
        messages.success(request,f' Application succefully Approved')
        return redirect('applications')
    else:
            context={
            
             'application' : application.objects.get(id=pk)
        }       
    return render(request,'applications/approval-form.html',context)


def reject_permit(request,pk):
    app = application.objects.get(id=pk)
    if request.method == 'POST':
        
        app.status = 'NotApproved'
        app.StatusReason =  request.POST.get('rejectreason')
        app.save()
        # subject = "New Notification - Perms"     
        # message = " Your application Has been Approved "
        # recipient_list = [app.user.email,]
        # send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently = False)
        messages.warning(request,f' Application succefully Rejected')
        return redirect('applications')
    else:
            context={
            
             'application' : application.objects.get(id=pk)
        }       
    return render(request,'applications/reject-form.html',context)



def payment(request,pk):
    app = application.objects.get(id=pk)
    if request.method == 'POST':
        
       
   
        messages.warning(request,f' Application succefully Rejected')
        return redirect('applications')
    else:
            context={
            
             'applicationdetails' : application.objects.get(id=pk)
        }       
    return render(request,'applications/payment-form.html',context)