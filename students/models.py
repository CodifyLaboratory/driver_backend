from django.db import models
from django.core.validators import RegexValidator
from group.models import Group


class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    serial_number = models.CharField(max_length=50)
    issued_by = models.CharField(max_length=50)
    inn = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators= [phoneNumberRegex], max_length=16, unique=True)
    is_active = models.BooleanField(default=False)
    is_graduated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class StudentGroup(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.PROTECT)
#     group = models.ForeignKey('group.Group', on_delete=models.PROTECT)
#
#     def __str__(self):
#         return f"({self.student}/{self.group})"
#
