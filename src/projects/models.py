from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from users.models import Landlord_Profile, Tenant_Profile
from projects.choices import *

# Create your models here.

class Property_Reviews(models.Model):
    tenant = models.ForeignKey(Tenant_Profile,to_field='tenant', on_delete=models.CASCADE)
    property = models.ForeignKey('Properties', on_delete=models.CASCADE, default=1)
    landlord = models.ForeignKey(Landlord_Profile,to_field='landlord', on_delete=models.CASCADE)
    review_description = models.TextField()


class Schedule_Viewing(models.Model):
    landlord = models.ForeignKey(Landlord_Profile,to_field='landlord', on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant_Profile,to_field='tenant', on_delete=models.CASCADE)
    listing = models.ForeignKey('Properties', on_delete=models.CASCADE)
    date = models.CharField(max_length=16,null=True)
    time = models.CharField(max_length=6,null=True)


class Property_Applications(models.Model):
     tenant_apply = models.ForeignKey(Tenant_Profile,to_field='tenant', on_delete=models.CASCADE)
     property_owner = models.ForeignKey(Landlord_Profile,to_field='landlord', on_delete=models.CASCADE)
     listing = models.ForeignKey('Properties', on_delete=models.CASCADE)
     app_description = models.TextField(default='app description')
     created = models.TextField(default=1)

class Properties(models.Model):
    User = settings.AUTH_USER_MODEL
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    street1 = models.CharField(max_length=20,null=True)
    street2 = models.CharField(max_length=20,null=True)
    county = models.CharField(choices=COUNTY_CHOICES,max_length=200)
    rentPrice = models.IntegerField()
    description = models.TextField(null=True)
    type = models.CharField(choices=TYPE_CHOICES,max_length=200,default='House')
    bedRooms = models.IntegerField(choices=NUMBER_CHOICES,default=1)
    bathRoom = models.IntegerField(choices=NUMBER_CHOICES,default=1)
    tenantSalary = models.IntegerField(null=True)
    referenceRequired = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.street1} Property'

class Property_Images(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    images = models.FileField(upload_to="house_preview/%Y/%m/%d", default=None)



