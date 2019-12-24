from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Gallery.as_view(), name='gallery'),
]