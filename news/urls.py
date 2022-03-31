from django.urls import path, include
from rest_framework import routers

from .views import NewsPostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('newspost', NewsPostViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
