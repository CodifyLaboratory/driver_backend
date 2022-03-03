from django.urls import path, include
from .views import Exam, RandomQuestion, ExamQuestion

app_name='test'

urlpatterns = [
    path('', Exam.as_view(), name='test'),
    path('re/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('qe/<str:topic>/', ExamQuestion.as_view(), name='questions'),
]

