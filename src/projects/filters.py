import django_filters
from .models import *
from django.forms.widgets import TextInput

class CountyFilter(django_filters.FilterSet):
    class Meta:
        # rentPrice = django_filters.NumberFilter()
        # price__gt = django_filters.NumberFilter(field_name='rentPrice', lookup_expr='gt')
        # price__lt = django_filters.NumberFilter(field_name='rentPrice', lookup_expr='lt')
        model = Properties
        fields = '__all__'
        exclude = ['image','tenantSalary','referenceRequired',
                     'street1','street2','description','landlord','rentPrice','listingStatus']
