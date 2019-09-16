from django.contrib import admin
from django.urls import path, include
from . import views, forms

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile_user, name='profile'),
    path('change_profile/', views.change_profile, name='change-profile'),
    # path('sign_in/', views.sign_in, name='sign_in')
]
