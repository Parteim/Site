from django.contrib import admin
from django.urls import path, include
from . import views, forms
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,

    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile_user, name='profile'),
    path('change_profile/', views.change_profile, name='change-profile'),

    # Url for password change and password reset
    # change
    path('password_change/',
         PasswordChangeView.as_view(template_name='user/password/password_change_form.html'),
         name='password_change'),
    path('password_change_done/',
         PasswordChangeDoneView.as_view(template_name='user/password/password_change_done.html'),
         name='password_change_done'),

    # reset
    path('password_reset/',
         PasswordResetView.as_view(template_name='user/password/password_reset_form.html'),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='user/password/password_reset_confirm.html'),
         name='password-reset-confirm'),
    path('password_reset_confirm/done/',
         PasswordResetDoneView.as_view(template_name='user/password/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='user/password/password_reset_complete.html'),
         name='password_reset_complete'),

]
