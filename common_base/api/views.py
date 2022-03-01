from common_base.models import CommonBase
from common_base.api.serializers import CommonBaseSerializer
from rest_framework import viewsets, permissions


class CommonBaseViewSet(viewsets.ModelViewSet):
    queryset = CommonBase.objects.all()
    serializer_class = CommonBaseSerializer
    permission_classes = [permissions.AllowAny]
