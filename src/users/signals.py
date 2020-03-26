from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Landlord_Profile


# This function aims to create a profile everytime a user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Landlord_Profile.objects.create(landlord=instance)

# kwargs just accepts any additional keyword arguments on the end of the function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.landlord_profile.save()
