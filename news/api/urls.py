from rest_framework import routers
from news.api.view_viewset import NewsViewset

news_router = routers.DefaultRouter()
news_router.register('news', NewsViewset, basename='News')
