from django.db import models
from user.models import CustomUser
from django.utils import timezone


class Case(models.Model):
    executor = models.CharField(max_length=150, verbose_name='Исполнитель')
    customer = models.CharField(max_length=150, verbose_name='Заказчик')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание кейса')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-instance', kwargs={'pk': self.pk})