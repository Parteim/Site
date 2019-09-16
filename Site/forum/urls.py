from . import views
from django.urls import path


urlpatterns = [
    # path('', views.ShowForumPage, name='forum'),
    path('', views.ForumPage.as_view(), name='forum'),
    path('forum/<int:pk>/', views.single_post, name='post-instance'),
    path('create_post/', views.CreateYourPost.as_view(), name='create-post'),
]