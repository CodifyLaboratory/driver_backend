from feedback.models import Feedback
from feedback.api.serializers import FeedbackSerializer
from rest_framework import viewsets, permissions


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]
