from feedback.models import Feedback
from feedback.api.serializers import FeedbackSerializer
from rest_framework import mixins, generics


class FeedbackCreateList(generics.GenericAPIView,
                           mixins.CreateModelMixin,
                           mixins.ListModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class FeedbackUpdateDeleteView(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request,  *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)