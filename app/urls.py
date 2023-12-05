from django.urls import path
from . import views

urlpatterns = [
    path("", views.teammembers, name="teammembers"),
    path("add_teammember/", views.add_teammember, name="add_teammember"),
]