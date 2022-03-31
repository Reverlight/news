from django.db import models


class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.IntegerField()
    author_name = models.CharField(max_length=255)
