from operator import mod
from statistics import mode
from django.db import models
from datetime import datetime


def image_save_path(instance, filename):
    return 'base/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)


class CommonBase(models.Model):
    title = models.CharField(max_length=100, verbose_name= "Название статьи")
    description = models.TextField(verbose_name="Описание статьи")
    image = models.ImageField(upload_to=image_save_path, null=True, verbose_name="Изображение")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "База знаний"
        ordering = ['-created_date']

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)
