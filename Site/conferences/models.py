from django.db import models
from django.utils import timezone


class Conferences(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(default='default/default_contests.jpg', upload_to='conferences')
    date = models.DateField(default=timezone.now)

    upcoming = 'Предстоящий'
    past = 'Прошедший'
    choice_status = (
        (upcoming, 'Предстоящий'),
        (past, 'Прошедший'),
    )

    status = models.CharField(max_length=100, choices=choice_status, default=upcoming)

    def __str__(self):
        return self.title


class ConferencesTopic(models.Model):
    conference = models.ForeignKey(Conferences, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    winner = 'Победитель'
    participant = 'Участник'
    choice_status = (
        (participant, 'Участник'),
        (winner, 'Победитель'),
    )
    status = models.CharField(max_length=100, choices=choice_status, default=participant)

    def __str__(self):
        return self.title
