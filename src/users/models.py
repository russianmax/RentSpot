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
    identification = models.FileField(upload_to='docs',null=True,blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_landlord = models.BooleanField(choices=usertypechoices,default=False)
    salary = models.FloatField(null=True)
    salaryDocument = models.FileField(upload_to='docs',null=True,blank=True)
    references = models.FileField(upload_to='docs',null=True, blank=True)
    savingsDocument = models.FileField(upload_to='docs',null=True,blank=True)
    is_hap = models.BooleanField(null=True)
    #NullBooleanField(default = False)
    hapDocument = models.FileField(upload_to='docs',null=True, blank=True)
    both_salary = models.IntegerField(null=True,default=None)

    def __str__(self):
        return f'{self.tenant.username} Tenant Profile'


class Landlord_Profile(models.Model):
    landlord = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.FileField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_landlord = models.BooleanField(choices=usertypechoices,default=True)
    street1 = models.CharField(max_length=20,null=True)
    street2 = models.CharField(max_length=20,null=True)
    county = models.CharField(max_length=20 ,null=True)
    postCode = models.CharField(max_length=20,null=True)


    def __str__(self):
        return f'{self.landlord.username} Landlord Profile'


class Guarantor(models.Model):
    tenant = models.OneToOneField('Tenant_Profile', on_delete=models.CASCADE)
    g_salary = models.FloatField(null=True)
    g_salaryDoc = models.FileField(upload_to='docs',null=True, blank=True)
    g_confirmation = models.FileField(upload_to='docs',null=True, blank=True)

    #