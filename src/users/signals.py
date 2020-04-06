from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tenant_Profile, Landlord_Profile


# This function aims to create a profile everytime a user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
     #if created:
         #Tenant_Profile.objects.create(tenant=instance)
     if created and User.last_name == False:
            Tenant_Profile.objects.create(tenant=instance)
     elif created and User.last_name == True:
             Landlord_Profile.objects.create(landlord=instance)



# kwargs just accepts any additional keyword arguments on the end of the function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    #instance.tenant_profile.save()
    if User.last_name == False:
        instance.tenant_profile.save()
    elif User.last_name == True:
        instance.landlord_profile.save()


