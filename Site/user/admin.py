from .models import CustomUser
from django.contrib import admin
from .models import Profile, StudentProfile, TeacherProfile

admin.site.register(Profile)
admin.site.register(StudentProfile)
admin.site.register(CustomUser)
admin.site.register(TeacherProfile)


class UserShowAdminPag(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
