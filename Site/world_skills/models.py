from django.db import models
from gallery.models import Photo
from django.utils import timezone


class WorldSkillsContest(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    # img = models.ImageField()
    img = models.ImageField(default='default/default_contests.jpg', upload_to='worldskills')
    date = models.DateField(default=timezone.now)

    upcoming = 'Предстоящий'
    past = 'Прошедший'
    choice_status = (
        (upcoming, 'Предстоящий'),
        (past, 'Прошедший'),
    )
    status = models.CharField(max_length=100, choices=choice_status, default=upcoming)

    data_about_contest = models.FileField(
        default='',
        upload_to='worldskills/file',
        blank=True, 
        null=True,
    )

    def __str__(self):
        return str(self.title)


class PastWorldSkillsContest(models.Model):
    past_contest = models.ForeignKey(WorldSkillsContest, on_delete=models.CASCADE)
    gallery_img = models.ImageField(upload_to='worldskills/img')
