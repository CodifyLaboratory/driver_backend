from django.db import models
from datetime import datetime


def image_save_path(instance, filename):
    return 'news/image/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)

def video_save_path(instance, filename):
    return 'news/video/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)

class News(models.Model):
    title = models.CharField(max_length=100)
    shot_description = models.CharField(max_length=300, null=True)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to=image_save_path, null=True, blank=True)
    video = models.FileField(upload_to=video_save_path, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Новости'
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
