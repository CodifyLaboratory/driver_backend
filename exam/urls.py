from django.urls import path
from .views import Exam, RandomQuestion, ExamQuestion, ExamTimer

app_name = 'exam'

urlpatterns = [
    path('', Exam.as_view(), name='exam'),
    path('re/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('qe/<str:topic>/', ExamQuestion.as_view(), name='questions'),
    path('t/', ExamTimer.as_view(), name='timer'),
]

