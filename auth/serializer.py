from django.contrib.auth.models import User
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    date_of_birtg = serializers.DateField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    serial_number = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    issued_by = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    inn = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )

    # name = models.CharField(max_length=100)
    # date_of_birth = models.DateField()
    # serial_number = models.CharField(max_length=50)
    # issued_by = models.CharField(max_length=50)
    # inn = models.CharField(max_length=20)
    # group = models.ForeignKey(Group, on_delete=models.PROTECT)
    # email = models.EmailField()
    # phoneNumberRegex = RegexValidator(regex= r"^\+?1?\d{8,15}$")
    # phoneNumber = models.CharField(validators= [phoneNumberRegex], max_length=16, unique=True)
    # is_active = models.BooleanField(default=False)
    # is_graduated = models.BooleanField(default=False)



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
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            password=validated_data["password"]

        )

        Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        token = Token.objects.filter(user_id=instance.id).first()
        response["token"] = token.key
        return response

