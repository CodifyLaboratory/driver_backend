from rest_framework import generics
from .models import Exam, Question, ExamTimer
from .serializers import ExamSerializer, RandomQuestionSerializer, QuestionSerializer, ExamTimerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Exam(generics.ListAPIView):

    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class RandomQuestion(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(exam__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class ExamQuestion(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(exam__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class ExamTimer(generics.ListAPIView):

    serializer_class = ExamTimerSerializer
    queryset = ExamTimer.objects.all()
