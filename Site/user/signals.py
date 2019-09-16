from .models import CustomUser, Profile, StudentProfile, TeacherProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def binding_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def binding_class_with_profile(sender, instance, created, **kwargs):
    if created:
        profile_user = CustomUser.objects.get(email=instance)
        print(profile_user)
        if profile_user.who_is == 'student':
            StudentProfile.objects.create(profile_user=instance)
        elif profile_user.user.who_is == 'teacher':
            TeacherProfile.objects.create(profile_user=instance)
