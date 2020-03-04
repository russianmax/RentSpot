from django.contrib import admin
from .models import Properties, Property_Applications, Property_Reviews

admin.site.register(Properties)
admin.site.register(Property_Applications)
admin.site.register(Property_Reviews)

# admin.site.register(Listing_Images)