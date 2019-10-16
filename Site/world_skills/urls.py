from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WorldSkills.as_view(), name='world-skills'),
    path('contest/<int:pk>/', views.InstanceWorldSkills.as_view(), name='world-skills-contest'),

]
