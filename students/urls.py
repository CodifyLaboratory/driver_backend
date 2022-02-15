from django.urls import path
from .views import StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
]
