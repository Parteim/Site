from django.db import models
from django.utils import timezone


class Contests(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    img = models.ImageField(default='default/default_contests.jpg', upload_to='contests')
    date = models.DateField(default=timezone.now)
    full_information_about_contest = models.FileField(default='', upload_to='contests/file', blank=True, null=True)

    def __str__(self):
        return self.title


class FutureContests(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    img = models.ImageField(default='default/default_contests.jpg', upload_to='contests')
    date = models.DateField(default=timezone.now)
    full_information_about_contest = models.FileField(default='', upload_to='contests/file', blank=True, null=True)

    def __str__(self):
        return self.title


class Winners(models.Model):
    title_contest = models.ForeignKey(Contests, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    img = models.ImageField(default='default/user_profile_img.png', upload_to='contests/winners')

    def __str__(self):
        return self.first_name


class PastContests(models.Model):
    title = models.ForeignKey(Contests, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(default='default/default_contests.jpg', upload_to='contests')
    date = models.DateField(default=timezone.now)
    winners = models.ForeignKey(Winners, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
