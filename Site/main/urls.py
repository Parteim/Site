from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowMainPage, name='home'),
    path('news/<int:pk>/', views.SingleShowNews.as_view(), name='news-instance'),
    path('news/', views.ShowNews.as_view(), name='news'),
    path('recipe/<int:pk>/', views.SingleShowRecipe.as_view(), name='recipe-instance'),
    path('recipe/', views.ShowRecipe.as_view(), name='recipe'),
]
