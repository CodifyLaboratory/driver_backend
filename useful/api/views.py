from rest_framework import mixins, generics
from useful.models import Useful
from useful.api.serializers import UsefulSerializer


class UsefulCreateListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UsefulUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


