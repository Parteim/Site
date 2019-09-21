from django.db import models
from django.utils import timezone
from user.models import CustomUser


class Contests(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    img = models.ImageField(default='default/default_contests.jpg', upload_to='contests')
    date = models.DateField(default=timezone.now)
    full_information_about_contest = models.FileField(default='', upload_to='contests/file', blank=True, null=True)

    upcoming = 'Предстоящий'
    past = 'Прошедший'
    choice_status = (
        (upcoming, 'Предстоящий'),
        (past, 'Прошедший'),
    )

    status = models.CharField(max_length=100, choices=choice_status, default=upcoming)
    # verbose_name
    def __str__(self):
        return self.title


class Participants(models.Model):
    contest = models.ForeignKey(Contests, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    winner = 'Победитель'
    participant = 'Участник'
    choice_status = (
        (participant, 'Участник'),
        (winner, 'Победитель'),
    )
    status = models.CharField(max_length=100, choices=choice_status, default=participant)

    def __str__(self):
        return str(self.user)
