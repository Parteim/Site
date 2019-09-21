from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowContestsPage,  name='contests'),
    path('all_contests', views.ShowContests.as_view(),  name='all-contests'),
    path('past_contests', views.ShowPastContests.as_view(),  name='past-contests'),
    path('contest/<int:pk>/', views.SingleShowContests.as_view(), name='contest-instance'),
    # path('past_contest/<int:pk>/', views.SingleShowPastContests.as_view(), name='past-contest-instance'),
]
