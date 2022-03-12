from django.db import models


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return '{0} {1} {2}'.format(self.first_name, self.last_name, self.middle_name)

