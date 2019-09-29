from .models import Contests, Participants
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=Participants)
def binding_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        send_mail(
            'Участник конкурса',
            '{} {} принял участие в конкурсе: {}'.format(
                instance.user.first_name,
                instance.user.last_name,
                instance.contest.title
            ),
            'Sergej_kajnov@mail.ru',
            'Parteim2.0@mail.ru',
        )
