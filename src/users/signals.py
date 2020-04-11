from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tenant_Profile, Landlord_Profile


# This function aims to create a profile everytime a user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.last_name == 'False':
            Tenant_Profile.objects.create(tenant=instance)
        else:
            Landlord_Profile.objects.create(landlord=instance)




