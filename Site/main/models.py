from django.db import models
from django.utils import timezone


class Ads(models.Model):
    title = models.CharField(max_length=100, default='Объявление')
    text = models.TextField()
    img = models.ImageField(default='default/default_ads.jpg', upload_to='ads')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(default='default/default_News.jpg', upload_to='news')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(default='default/recipe__image.png', upload_to='recipe')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
