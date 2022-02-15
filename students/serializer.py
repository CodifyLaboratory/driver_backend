from rest_framework import serializers
from .models import Student
from django.core.validators import RegexValidator
from groups.models import Group


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    serial_number = serializers.CharField(max_length=50)
    issued_by = serializers.CharField(max_length=50)
    inn = serializers.CharField(max_length=20)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    email = serializers.EmailField()
    phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
    phoneNumber = serializers.CharField(validators= [phoneNumberRegex], max_length=16)
    is_active = serializers.BooleanField(default=False)
    is_graduated = serializers.BooleanField(default=False)

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)

        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.serial_number = validated_data.get('serial_number', instance.serial_number)
        instance.issued_by = validated_data.get('issued_by', instance.issued_by)
        instance.inn = validated_data.get('inn', instance.inn)
        instance.group = validated_data.get('group', instance.group)
        instance.email = validated_data.get('email', instance.email)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_graduated = validated_data.get('is_graduated', instance.is_graduated)
        instance.save()
        return instance



