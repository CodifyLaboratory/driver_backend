from common_base.models import CommonBase
from common_base.api.serializers import CommonBaseSerializer
from rest_framework import mixins, generics


class CommonBaseCreateList(generics.GenericAPIView,
                           mixins.CreateModelMixin,
                           mixins.ListModelMixin):
    queryset = CommonBase.objects.all()
    serializer_class = CommonBaseSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CommonBaseUpdateDeleteView(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    queryset = CommonBase.objects.all()
    serializer_class = CommonBaseSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request,  *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)