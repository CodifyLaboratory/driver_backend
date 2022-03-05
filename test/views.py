from rest_framework import generics
from .models import Test, Question
from .serializers import TestSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Test(generics.ListAPIView):

    serializer_class = TestSerializer
    queryset = Test.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(test__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class TestQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(test__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

