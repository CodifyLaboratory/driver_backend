from rest_framework import routers
from feedback.api.views import FeedbackViewSet

base_router = routers.DefaultRouter()
base_router.register('feedback', FeedbackViewSet, basename='Feedback')