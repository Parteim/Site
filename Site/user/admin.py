from .models import CustomUser
from django.contrib import admin
from .models import Profile, StudentProfile

admin.site.register(Profile)
admin.site.register(StudentProfile)
admin.site.register(CustomUser)


class UserShowAdminPag(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
