from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(application)

class applicationadmin(admin.ModelAdmin):
    list_display = ('user','permit_number','date_created','status','date_approved')
admin.site.register(application,applicationadmin)
