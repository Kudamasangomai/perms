from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nationalid','role','user_phone')
admin.site.register(profile, ProfileAdmin)

