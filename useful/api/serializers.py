from rest_framework import serializers
from useful.models import Useful


class UsefulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useful
        fields = '__all__'