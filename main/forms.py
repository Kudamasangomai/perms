from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from farmers.models import farmer
from users.models import profile




class UserRegisterForm(UserCreationForm):
      
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15,min_length=3)
    last_name = forms.CharField(min_length=3,max_length=15)

    #the model in which this form is going to interact with
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    
	email = forms.EmailField()
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={

		"readonly":'readonly'
		}))
	class Meta:
		model = User
		fields = ['email','username','first_name','last_name']

class profileupdateform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image','user_phone']



class adminprofileupdateform(forms.ModelForm):
     class Meta:
            model = profile
            fields = '__all__'

class RegisterFarmerForm(forms.ModelForm):
    class Meta:
        model = farmer
        fields ='__all__'
        exclude = ['fuser','date_created']