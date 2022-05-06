from tabnanny import verbose
from django.db import models
from about_user.models import About
from useful.models import Useful


class Comment(models.Model):
    article = models.ForeignKey(Useful, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(About, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        verbose_name = 'Комментарии'
        ordering = ('-created_date',)

    def __str__(self):
        return 'Comment by {}'.format(self.author.first_name +' '+ self.author.last_name)
