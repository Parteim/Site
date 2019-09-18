from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.conferences, name='conferences'),
    path('past_conferences/', views.AllPastConferences.as_view(), name='past-conferences'),
    path('conference/<int:pk>/', views.SingleShowConference.as_view(), name='conference'),
]