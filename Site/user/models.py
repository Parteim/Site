from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django import forms
from PIL import Image


class CustomUser(AbstractUser):
    first_name = models.CharField(_('Имя'), max_length=100, unique=False)
    last_name = models.CharField(_('Фамилия'), max_length=100, unique=False)
    email = models.EmailField(_('E-mail'), unique=True)
    username = models.CharField(max_length=40, unique=False, default='')

    choose_who_is = (
        ('student', 'Студент'),
        ('teacher', 'Учитель'),
        ('none', 'Не указан'),
    )

    who_is = models.CharField(max_length=50, choices=choose_who_is, default='Не указан')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    img = models.ImageField(default='default/user_profile_img.png', upload_to='profile')

    def __str__(self):
        return f'{self.user.email}'


class StudentProfile(models.Model):
    profile_user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    course = models.PositiveIntegerField(default=0)
    faculty = models.CharField(max_length=150, default='Не указан')

    def __str__(self):
        return f'{self.profile_user}'


class TeacherProfile(models.Model):
    profile_user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='Учитель')

    def __str__(self):
        return f'{self.profile_user}'
