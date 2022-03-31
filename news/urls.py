from django.urls import path, include
from rest_framework import routers

from .views import NewsPostViewSet, CommentViewSet, NewsPostUpvote


router = routers.DefaultRouter()
router.register('newspost', NewsPostViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('upvote/<int:pk>/', NewsPostUpvote.as_view())
]
