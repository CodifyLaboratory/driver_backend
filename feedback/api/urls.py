from rest_framework import routers
from feedback.api.views import FeedbackViewSet

feedback_router = routers.DefaultRouter()
feedback_router.register('feedback', FeedbackViewSet, basename='Feedback')