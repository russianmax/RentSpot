import django_filters
from .models import *
from django.forms.widgets import TextInput

# django query based filter form
class Filter(django_filters.FilterSet):
    class Meta:
        model = Properties
        # all fields
        fields = '__all__'
        # excludes the following
        exclude = ['image','tenantSalary','referenceRequired',
                     'street1','street2','description','landlord','rentPrice','listingStatus']
