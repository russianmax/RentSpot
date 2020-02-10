from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile
from django.forms import ModelForm
# from .models import usertypechoices

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # usertype = forms.ChoiceField(choices=usertypechoices)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class to allow user update their own data
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['usertype','image']

