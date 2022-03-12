from django.db import models
from datetime import datetime
from user.models import User

def image_save_path(instance, filename):
    return 'lesson/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)


class Lesson(models.Model):
    title= models.CharField(max_length=150, verbose_name="Название урока")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    image = models.ImageField(upload_to=image_save_path, null=True, verbose_name="Изображение")
    views = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='lessons')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Уроки")
        ordering = ['id']
    
    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

