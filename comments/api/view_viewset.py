from rest_framework import viewsets, permissions
from comments.models import Comment
from comments.api.serializers import CommentSerializer


class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =  [permissions.AllowAny]
