from django.db import models


class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvote_amount = models.IntegerField(blank=True, default=0)
    author_name = models.CharField(max_length=255)
