from django.urls import path
from .views import Test, RandomQuestion, TestQuestion

app_name='test'

urlpatterns = [
    path('', Test.as_view(), name='test'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', TestQuestion.as_view(), name='questions'),
]

