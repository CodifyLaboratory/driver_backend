from rest_framework import routers
from comments.api.view_viewset import CommentsViewset

comments_router = routers.DefaultRouter()
comments_router.register('comments', CommentsViewset, basename='Comments')