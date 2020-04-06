from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Tenant_Profile
from django.forms import ModelForm
from .models import usertypechoices

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    whatisthis = forms.ChoiceField(choices=usertypechoices)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','whatisthis']


# class to allow user update their own data
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email',]

# Set profile variables in Update profile page for tenants
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Tenant_Profile
        fields = ['is_landlord','image','salary','savings','is_hap']


