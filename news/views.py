from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import NewsPost, Comment
from news.serializers import NewsPostSerializer, CommentSerializer


class NewsPostViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class NewsPostUpvote(APIView):
    serializer = NewsPostSerializer

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = NewsPost.objects.get(id=post_id)
        post.upvote_post()

        serializer = self.serializer(post)
        return Response(serializer.data)