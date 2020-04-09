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
    salary_doc = models.FilePathField(null=True)
    savings = models.FloatField(null=True)
    savings_doc = models.FilePathField(null=True)
    is_hap = models.NullBooleanField(default=False)

    def __str__(self):
        return f'{self.tenant.username} Tenant Profile'

    # Resize images to reduce memory wasted
    def save(self, *args, **kwargs):
        super(Tenant_Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Landlord_Profile(models.Model):
    landlord = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_landlord = models.BooleanField(choices=usertypechoices,default=True)


    def __str__(self):
        return f'{self.landlord.username} Landlord Profile'