from .models import *
from main.forms import *
from requests import request
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView ,UpdateView,DeleteView,FormView,DetailView,CreateView


# Create your views here.
class ApplicationsliStView(LoginRequiredMixin, ListView):
    model = application
    #context_object_name = 'applications'
    template_name = 'applications/applications-list.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationsliStView,self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
             context['applications'] = application.objects.all()
        else:
            context['applications'] = application.objects.filter(user = self.request.user)
        return context



class ApplyPermitView(LoginRequiredMixin, CreateView):
    model = application
    form_class = PermitApplicationForm
    template_name = 'applications/application-form.html'
    success_url = reverse_lazy('applications')
