from django.db import models
from PIL import Image
from django.urls import reverse
from django.utils import timezone


class Photo(models.Model):
    description = models.CharField(max_length=200, blank=True, default='')
    img = models.ImageField(upload_to='gallery')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('gallery', args=[self.pk])

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super().save()
    #
    #     path = self.img.path
    #
    #     image = Image.open(path)
    #
    #     if image.height > 64 or image.width > 64:
    #         resize = (64, 64)
    #         image.thumbnail(resize)
    #         image.save(path)
