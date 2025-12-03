from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.teams, name='teams'),
    path("teams_details/<int:member_id>/", views.team_member_detail, name="team_member_detail"),
]
