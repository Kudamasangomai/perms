import time
from .models import *
from main.forms import *
from paynow import Paynow
from farmers.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import datetime ,timedelta
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView ,UpdateView,DeleteView,DetailView,CreateView


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

class ApplicationUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = application
    form_class = PermitApplicationForm
    template_name = 'applications/application-form.html' 
    success_message = " Permit Succesfully Updated"  
    success_url = reverse_lazy('applications')



class ApplicantView(LoginRequiredMixin,DetailView):
    model = application
    template_name = 'applications/applicant_verification.html'


@login_required
def assign_officer(request,pk):
    app = application.objects.get(id=pk)
    appwoner = User.objects.get(id=app.user_id)
    appofficerid = request.POST.get('officerid')
    

    if request.user.is_staff == True:
        
        if request.method == 'POST':
            user = User.objects.get(id=appofficerid )
            app.Approving_officer = user
            app.status = 'Processing'
            app.save()
            # subject = "New Notification - Perms"        
            # message = " Your application in Now being proccesed "
            # recipient_list = [appwoner.email,]
            # send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently = False)
            # messages.success(request,f' Application succefully Assigned')
            return redirect('applications')
        
        else:
            context={
                'officer' : User.objects.all(),
                'application' : application.objects.get(id=pk)
            }       
            return render(request,'applications/assign-form.html',context)
    return render(request,'main/page_not_found.html')



@login_required
def approve_permit(request,pk):
    app = application.objects.get(id=pk)
    expirydate = datetime.today() + timedelta(days=365)
    
    if request.user.is_staff == True:
        if request.method == 'POST':
            
            app.status = 'Approved'
            app.StatusReason =  'Approved'
            app.Expiry_of_permit_date = expirydate
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
    return render(request,'main/page_not_found.html')

@login_required
def reject_permit(request,pk):
    app = application.objects.get(id=pk)
    if request.user.is_staff == True:
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
    return render(request,'main/page_not_found.html')

@login_required
def payment(request,pk):
    app = application.objects.get(id=pk)
    context={
            
             'applicationdetails' : application.objects.get(id=pk)
        }       
    return render(request,'applications/payment-form.html',context)


@login_required
def process_payment(request):
    #app = application.objects.get(id=pk)
    timeout = 10
    retries = 0
    sleep_time = 10

    if request.method == 'POST':
        usern = request.POST.get('ecocashnumber')
        #amount =float( request.POST.get('amount'))
        amount = 1
        returnUrl ='http://google.com'
        returnUrl ='http://google.com'
        print(usern)
        paynow = Paynow(
           
            '13396',
            'af269a2d-c734-4a6a-aa2a-c96aa73fb4d3',
            returnUrl,
            returnUrl
            )
        
        payment = paynow.create_payment('Order', 'masboyk@gmail.com')
        payment.add('Payment for Permit licence', amount )
        response = paynow.send_mobile(payment, usern, 'ecocash')
        
        
       
        if(response.success):            
            poll_url = response.poll_url
            print("Poll Url: ", poll_url)

        while retries < timeout:
            time.sleep(sleep_time)
            status = paynow.check_transaction_status(poll_url)

            if status.paid :
                #print('Yay! Transaction was paid for. Update transaction')
                #redirect_to = request.POST.get('next', request.user.id)
                messages.success(request, f'Transaction Was Succesfull')
                #return redirect('submit-pay', redirect_to)
                context = {
                    'paid' : status.paid
                }
                return render(request,'applications/applications-list.html',context)
            else:
                print(status.paid)
                #redirect_to = request.POST.get('next', request.user.id)
                messages.warning(request, f'Transaction Fail please try again')
                #return redirect('payment', redirect_to)
                return render(request,'applications/applications-list.html',context)
                  
        retries = retries + 1
  