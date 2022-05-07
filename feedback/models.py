from django.db import models
from about_user.models import About



class Feedback(models.Model):
    text = models.TextField()
    author = models.ForeignKey(About, on_delete=models.CASCADE, related_name='feedbacks')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Отзывы'
        # sort comments in chronological order by default
        ordering = ('-created_date',)

    def __str__(self):
        return 'Отзыв оставил {}'.format(self.author.first_name +' '+ self.author.last_name)
