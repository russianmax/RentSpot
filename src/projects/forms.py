from .models import Properties, Property_Applications, Property_Reviews
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# class to allow user update their own data
class CreatingListingForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['address', 'rentPrice','description','bedRooms','bathRoom','tenantCondtions','image']

class ListingApplicationForm(forms.ModelForm):
    class Meta:
        model = Property_Applications
        fields = ['app_description']

class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = Property_Reviews
        fields = ['review_description']