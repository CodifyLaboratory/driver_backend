from rest_framework import routers
from . view_viewset import CommentsViewset

comments_router = routers.DefaultRouter()
comments_router.register('comments', CommentsViewset, basename='Comments')
