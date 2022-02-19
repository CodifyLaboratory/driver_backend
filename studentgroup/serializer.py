from rest_framework import serializers
from .models import StudentGroup


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGroup
        fields = ['id', 'name', 'is_active', 'price', 'duration', 'max_students']
