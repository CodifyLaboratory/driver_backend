from rest_framework import viewsets, permissions
from useful.models import Useful
from useful.api.serializers import UsefulSerializer
from rest_framework import filters


class UsefulViewset(viewsets.ModelViewSet):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']