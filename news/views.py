from rest_framework import viewsets

from news.models import NewsPost
from news.serializers import NewsPostSerializer


class NewsPostViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

