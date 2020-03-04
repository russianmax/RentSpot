from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from users.models import Landlord_Profile, Tenant_Profile

# Create your models here.

class Property_Reviews(models.Model):
    tenant = models.ForeignKey(Tenant_Profile, on_delete=models.CASCADE)
    property = models.ForeignKey('Properties', on_delete=models.CASCADE, default=1)
    # landlord = models.OneToOneField(Landlord_Profile, on_delete=models.CASCADE)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Property_Applications(models.Model):
    User = settings.AUTH_USER_MODEL
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listingId = models.ForeignKey('Properties', on_delete=models.CASCADE)
    app_description = models.TextField(null=True)


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

