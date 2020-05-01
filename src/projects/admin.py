from django.contrib import admin
from .models import Properties, Property_Applications, Property_Reviews, Schedule_Viewing, Property_Images


admin.site.register(Properties)
admin.site.register(Property_Applications)
admin.site.register(Property_Reviews)
admin.site.register(Schedule_Viewing)
admin.site.register(Property_Images)

