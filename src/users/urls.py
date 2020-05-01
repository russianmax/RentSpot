from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("<int:pk>/<int:listing>", views.viewProfile, name="view_profile"),

] 
