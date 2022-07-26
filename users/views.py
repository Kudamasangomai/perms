from django.views.generic import(ListView,DetailView,FormView,UpdateView ,DeleteView,CreateView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from main.forms import *
from .models import *





# Create your views here.
class UserRegistrationView(CreateView,SuccessMessageMixin):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register_user.html'
    success_message = 'User Succesfully Created'   
    success_url=  '/'

class Userslistview(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    paginate_by = 5

    def get_queryset(self,**kwargs):
        return User.objects.filter(is_staff = True)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView,self).get_context_data(**kwargs)
       # context['userdetails'] = User.objects.filter(id = self.request.user.id)
        context['userdetails'] = documents.objects.filter(fuserd =self.request.user)
        return context
    
   


def admin_userprofile_update(request,pk):
    userdata = User.objects.get(id=pk)
   
    if request.method == 'POST':
        form = adminprofileupdateform(request.POST ,instance = User.objects.get(id=pk))
        profile_form = profileupdateform(request.POST,request.FILES , instance = profile.objects.get(user= userdata.id))

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request,f'Profile has been updated')
            return redirect('users')		
    else:
        form = adminprofileupdateform(instance = User.objects.get(id=pk))
        profile_form = profileupdateform(instance = profile.objects.get(user = userdata.id))

        context = {
        'form':form,
        'profile_form':profile_form 
         }
        return render(request,'users/admin_user_update.html',context)

def profile_edit(request,**kwargs):
	if request.method == 'POST':
		form = UserUpdateForm(request.POST ,instance = request.user)
		profile_form = profileupdateform(request.POST,request.FILES ,instance = request.user.profile)

		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			messages.success(request,f'Your profile has been updated')
			return redirect('user-profile')
		

	else:
		form = UserUpdateForm(instance = request.user)
		profile_form = profileupdateform(instance = request.user.profile)

		context = {
        'update_form':form,
        'profile_form':profile_form 
    }
		return render(request,'users/user_profile_edit.html',context)
