from .models import Properties, Property_Applications, Property_Reviews, Schedule_Viewing, Property_Images
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ClearableFileInput

# class to allow user update their own data
class CreatingListingForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['image','street1','street2','county','type',
                  'description','bedRooms','bathRoom',
                  'rentPrice','tenantSalary','referenceRequired']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Property_Images
        fields = ['images']
        widgets = {'images': ClearableFileInput(attrs={'multiple': True}),}
        # widget is important to upload multiple files

class ListingApplicationForm(forms.ModelForm):
    class Meta:
        model = Property_Applications
        fields = ['app_description']

class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = Property_Reviews
        fields = ['review_description']

class ScheduleViewingForm(forms.ModelForm):
    class Meta:
        model = Schedule_Viewing
        fields = ['date','time']

class ManageListingForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['description','rentPrice','tenantSalary','referenceRequired','image']
