from rest_framework import viewsets

from news.models import NewsPost, Comment
from news.serializers import NewsPostSerializer, CommentSerializer


class NewsPostViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
