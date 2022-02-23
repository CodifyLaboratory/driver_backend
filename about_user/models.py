from django.db import models
from django.core.validators import RegexValidator
from studentgroup.models import StudentGroup


class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    serial_number = models.CharField(max_length=50)
    issued_by = models.CharField(max_length=50)
    inn = models.CharField(max_length=20)
    StudentGroup = models.ForeignKey(StudentGroup, on_delete=models.PROTECT)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)

    def __str__(self):
        return self.first_name
