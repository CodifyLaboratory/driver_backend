from rest_framework import viewsets, permissions, filters
from news.models import News
from news.api.serializers import NewsSerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
