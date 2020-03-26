from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Landlord_Profile
from django.forms import ModelForm

usertypechoices = [(True,'Landlord'),(False,'Tenant')]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    usertype = forms.ChoiceField(choices=usertypechoices)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class to allow user update their own data
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Landlord_Profile
        fields = ['usertype','image']

