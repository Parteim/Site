from django.db import models
from django.utils import timezone
from user.models import CustomUser
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(default='', upload_to='forum/img', blank=True, null=True)
    file = models.FileField(default='', upload_to='forum/file', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-instance', kwargs={'pk': self.pk})


class Comment(models.Model):
    for_this = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('post-instance', args=[self.for_this.pk])
