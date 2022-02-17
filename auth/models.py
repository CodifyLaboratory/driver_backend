from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from group.models import Group


class MyUser(AbstractUser):
    username = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    serial_number = models.CharField(max_length=50)
    issued_by = models.CharField(max_length=50)
    inn = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)

    class Meta:
        app_label = 'MyUser'

    def __str__(self):
        return self.username


def user_create(sender, **kwargs):
    print(sender)
    print(**kwargs)


post_save.connect(user_create, sender=AbstractUser)



