from django.shortcuts import render
from django.views.generic import ListView ,UpdateView,DeleteView,FormView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ApplicationsliStView(LoginRequiredMixin, ListView):
    template_name = 'applications/applications-list.html'