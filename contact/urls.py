from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path("contact/<int:contact_id>/", views.contact_details, name="contact_details")
] 
