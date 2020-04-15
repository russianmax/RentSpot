from django.db import models
from django.contrib.auth.models import User
from PIL import Image

usertypechoices = [(True,'Landlord'),(False,'Tenant')]

class Tenant_Reviews(models.Model):
    landlord = models.ForeignKey('Landlord_Profile', on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant_Profile', on_delete=models.CASCADE)
    review = models.TextField()
    stars = models.IntegerField(default=5)
    created_on = models.DateTimeField(auto_now_add=True)

class Tenant_Profile(models.Model):
    tenant = models.OneToOneField(User, on_delete=models.CASCADE, unique = True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_landlord = models.BooleanField(choices=usertypechoices,default=False)
    salary = models.FloatField(null=True)
    savings = models.FloatField(null=True)
    is_hap = models.NullBooleanField(default=False)

    def __str__(self):
        return f'{self.tenant.username} Tenant Profile'


class Landlord_Profile(models.Model):
    landlord = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_landlord = models.BooleanField(choices=usertypechoices,default=True)


    def __str__(self):
        return f'{self.landlord.username} Landlord Profile'