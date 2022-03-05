from rest_framework import viewsets
from .serializer import AboutSerializers
from .models import About


class AboutUserViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializers
    queryset = About.objects.all()

