from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from exam import views as exam_views
from case import views as case_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('user.urls')),
    path('sign_in/', views.LoginView.as_view(template_name='user/sign_in.html'), name='sign_in'),
    path('logout/', views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('contests/', include('contests.urls')),
    path('forum/', include('forum.urls')),
    path('gallery/', include('gallery.urls')),
    path('conferences/', include('conferences.urls')),
    path('world_skills/', include('world_skills.urls')),
    path('exam/', exam_views.exam_page, name='exam'),
    path('case/', case_views.CasePage.as_view(), name='case'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
