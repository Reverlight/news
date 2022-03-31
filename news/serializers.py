from rest_framework import serializers

from .models import NewsPost, Comment


class NewsPostSerializer(serializers.ModelSerializer):
    upvote_amount = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = NewsPost
        fields = ['title', 'link', 'author_name', 'created_at', 'upvote_amount']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author_name', 'content', 'created_at']