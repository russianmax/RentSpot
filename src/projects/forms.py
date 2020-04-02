from .models import Properties
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# class to allow user update their own data
class CreatingListingForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['address', 'rentPrice','description','bedRooms','bathRoom','tenantCondtions','image']
        