from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("<int:pk>/", views.viewProfile, name="view_profile"),
    path("portal/<int:pk>/", views.landlordPortal, name ="portal"),
] 
