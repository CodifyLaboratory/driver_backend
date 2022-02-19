from rest_framework import serializers
from .models import About


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ["id",
                  "first_name",
                  "last_name",
                  "date_of_birth",
                  "serial_number",
                  "issued_by",
                  "inn",
                  "StudentGroup",
                  "email",
                  "phoneNumber",
                  ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        issued_by = attrs["issued_by"]

        if issued_by[0] != "M":
            raise serializers.ValidationError(detail="Формат ввода не верен: MKK 217041", code="Отлично")

        return attrs

