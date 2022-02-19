from django.db import models

from django.core.validators import MaxValueValidator


class StudentGroup(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    duration = models.IntegerField()
    max_student = models.PositiveSmallIntegerField(validators=[MaxValueValidator])

    def __str__(self):
        return self.name
