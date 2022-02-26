from django.db import models
# from education_base.models import Lesson
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# class Question(models.Model):
#     title = models.CharField(max_length=255)
#
#
# class Answer(models.Model):
#     answer = models.CharField(max_length=255)
#
#
# class Test(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.PROTECT)
#     answer = models.ForeignKey(Answer, on_delete=models.PROTECT)
#


def image_save_path(instance, filename):
    return 'test/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)


class Test(models.Model):
    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_("New Test"), verbose_name=_('Test Title'))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _("Easy")),
        (1, _("Normal")),
        (2, _("Hard")),
    )

    TYPE = (
        (0, _("Multiple Choice")),
    )

    test = models.ForeignKey(
        Test, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(
        max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(
        default=False)

    def __str__(self):
        return self.answer_text


