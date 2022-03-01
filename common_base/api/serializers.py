from rest_framework import serializers
from common_base.models import CommonBase


class CommonBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonBase
        fields = '__all__'