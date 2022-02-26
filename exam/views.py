from rest_framework import generics
from .models import Exam, Question
from .serializers import ExamSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Exam(generics.ListAPIView):

    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(exam__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class ExamQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(exam__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

