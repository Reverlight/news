from django.db import models


class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvote_amount = models.IntegerField(blank=True, default=0)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def upvote_post(self):
        self.upvote_amount += 1
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name
