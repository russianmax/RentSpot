from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from users.models import Landlord_Profile, Tenant_Profile

# Create your models here.

class Property_Reviews(models.Model):
    tenant = models.ForeignKey(Tenant_Profile, on_delete=models.CASCADE,default=1)
    property = models.ForeignKey('Properties', on_delete=models.CASCADE, default=1)
    landlord = models.OneToOneField(Landlord_Profile, on_delete=models.CASCADE,default=1)
    review = models.TextField()
    created = models.TextField(default=1)

class Property_Applications(models.Model):
     tenant_apply = models.ForeignKey(Tenant_Profile, on_delete=models.CASCADE)
     property_owner = models.ForeignKey(Landlord_Profile, on_delete=models.CASCADE,default=1)
     listing = models.ForeignKey('Properties', on_delete=models.CASCADE)
     app_description = models.TextField(default='app description')
     created = models.TextField(default=1)

class Properties(models.Model):
    User = settings.AUTH_USER_MODEL
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    rentPrice = models.FloatField()
    description = models.TextField()
    bedRooms = models.IntegerField()
    bathRoom = models.IntegerField()
    tenantCondtions = models.CharField(max_length=100)
    image = models.ImageField(upload_to='house_preview/')

    def __str__(self):
        return f'{self.address} Property'

    def save(self, *args, **kwargs):
        super(Properties, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # if img.height > 500 or img.width > 600:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)


