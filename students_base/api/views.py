from students_base.api.serializers import LessonSerializer
from students_base.models import Lesson
from rest_framework import generics
from rest_framework.views import APIView


class LessonView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer