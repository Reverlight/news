from rest_framework import serializers

from .models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):
    upvote_amount = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = NewsPost
        fields = ['title', 'link', 'author_name', 'created_at', 'upvote_amount']
