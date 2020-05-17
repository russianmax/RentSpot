from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tenant_Profile, Landlord_Profile


# this function creates a profile Tenant or Landlord profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # once auth_users instance created, Tenant or Landlord profile is created off that
    if created:
        if instance.last_name == 'False':
            # creates a tenant profile
            Tenant_Profile.objects.create(tenant=instance)
        else:
            # creates a landlord profile
            Landlord_Profile.objects.create(landlord=instance)




