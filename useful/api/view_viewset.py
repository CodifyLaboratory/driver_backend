from rest_framework import viewsets, permissions
from useful.models import Useful
from useful.api.serializers import UsefulSerializer

class UsefulViewset(viewsets.ModelViewSet):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer
    permission_classes =  [permissions.AllowAny]