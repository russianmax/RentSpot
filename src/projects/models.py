from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

# class Project(models.Model):
#     address = models.CharField(max_length=100)
#     rentPrice = models.IntegerField()
#     description = models.TextField()
#     bedRooms = models.IntegerField()
#     bathRoom = models.IntegerField()
#     tenantCondtions = models.CharField(max_length=100)
#     image = models.ImageField(default='default.jpg', upload_to='house_preview')

class Listing_Database(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    rentPrice = models.IntegerField()
    description = models.TextField()
    bedRooms = models.IntegerField()
    bathRoom = models.IntegerField()
    tenantCondtions = models.CharField(max_length=100)
    image = models.ImageField(upload_to='house_preview/')


    def __str__(self):
        return f'{self.address} Listing'

    def save(self, *args, **kwargs):
        super(Listing_Database, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # if img.height > 500 or img.width > 600:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)

# class Listing_Images(models.Model):
#     image = models.ImageField(default='default.jpg', upload_to='house_preview')
#     listingId = models.ManyToManyField('Listing_Database', related_name='listing_form')

#     def __str__(self):
#         return f'{self.listingId} Listing'

#     def save(self, *args, **kwargs):
#         super(Listing_Images, self).save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         # if img.height > 500 or img.width > 600:
#         output_size = (50,50)
#         img.thumbnail(output_size)
#         img.save(self.image.path)


