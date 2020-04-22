from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Tenant_Profile, Landlord_Profile, Guarantor
from django.forms import ModelForm
from .models import usertypechoices

class UserRegistrationForm(UserCreationForm):
    #email = forms.EmailField()
    last_name = forms.ChoiceField(choices=usertypechoices)
    class Meta:
        model = User
        fields = ['username','password1', 'password2','last_name']


# class to allow user update their own data
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email',]

# Set profile variables in Update profile page for tenants
class TenantProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Tenant_Profile
        fields = ['identification','image','references','salary','salaryDocument','savings','savingsDocument','is_hap','hapDocument']

class AddGuarantorForm(forms.ModelForm):
    class Meta:
        model = Guarantor
        fields = ['g_salary','g_salaryDoc','g_confirmation']


class LandlordProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Landlord_Profile
        fields = ['identification','image','street1','street2','county','postCode']



