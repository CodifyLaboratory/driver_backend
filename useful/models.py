from django.db import models
from datetime import datetime


def image_save_path(instance, filename):
    return 'useful/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)


class Useful(models.Model):
    title = models.CharField(max_length=100)
    shot_description = models.CharField(max_length=300, null=True)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to=image_save_path, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
