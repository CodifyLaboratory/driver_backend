from django.contrib.auth.models import AbstractUser
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token
from group.models import Group
from django.core.validators import RegexValidator
from .models import MyUser


class MyUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    serial_number = serializers.CharField(max_length=50)
    issued_by = serializers.CharField(max_length=50)
    inn = serializers.CharField(max_length=20)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    email = serializers.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = serializers.CharField(validators=[phoneNumberRegex], max_length=16)
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True, min_length=8, write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]
        if password != confirm_password:
            raise serializers.ValidationError(detail="Пароль не совпадает", code="password_match")
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data['username'],
            date_of_birth=validated_data['date_of_birth'],
            serial_number=validated_data['serial_number'],
            issued_by=validated_data['issued_by'],
            inn=validated_data['inn'],
            group=validated_data['group'],
            email=validated_data['email'],
            phoneNumber=validated_data['phoneNumber'],
            password=validated_data['password']
        )

    # def create(self, validated_data):
    #     user = MyUser.objects.create(**validated_data)
    #
        Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        token = Token.objects.filter(user_id=instance.id).first()
        response["token"] = token.key
        return response




# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(
#         required=True, validators=[validators.UniqueValidator(queryset=AbstractUser.objects.all())]
#     )
#     date_of_birth = serializers.DateField(
#         required=True, validators=[validators.UniqueValidator(queryset=AbstractUser.objects.all())]
#     )
#     serial_number = serializers.CharField(
#         required=True, validators=[validators.UniqueValidator(queryset=AbstractUser.objects.all())]
#     )
#     issued_by = serializers.CharField(
#         required=True, validators=[validators.UniqueValidator(queryset=AbstractUser.objects.all())]
#     )
#     inn = serializers.CharField(
#         required=True, validators=[validators.UniqueValidator(queryset=AbstractUser.objects.all())]
#     )
#     group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), write_only=True)
#     email = serializers.EmailField(
#         required=True,
#         validators=[validators.UniqueValidator(queryset=AbstractUser.objects.all())]
#     )
#     phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
#     phoneNumber = serializers.CharField(validators= [phoneNumberRegex], max_length=16)


#
#     def create(self, validated_data):
#         user = AbstractUser.objects.create_user(
#             username=validated_data['username'],
#             date_of_birth=validated_data['date_of_birth'],
#             serial_number=validated_data['serial_number'],
#             issued_by=validated_data['issued_by'],
#             inn=validated_data['inn'],
#             group=validated_data['group'],
#             email=validated_data['email'],
#             phoneNumber=validated_data['phoneNumber'],
#             password=validated_data['password']
#         )

