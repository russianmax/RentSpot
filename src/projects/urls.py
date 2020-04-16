from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("createListing", views.createListing, name="createListing"),
    path("application_submit/<int:pk>/", views.property_apply, name="application_submit"),
    path("review_submit/<int:pk>/", views.property_review, name="review_submit"),
] 
