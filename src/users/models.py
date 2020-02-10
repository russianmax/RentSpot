from django.db import models
from django.contrib.auth.models import User
from PIL import Image

usertypechoices = [(True,'Landlord'),(False,'Tenant')]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    usertype = models.BooleanField(choices=usertypechoices,default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    # Resize images to reduce memory wasted
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)