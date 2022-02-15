from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name', 'is_active', 'price', 'duration', 'max_students']
