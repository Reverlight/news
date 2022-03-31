from django.urls import path, include
from rest_framework import routers

from .views import NewsPostViewSet

router = routers.SimpleRouter()
router.register('newspost', NewsPostViewSet)

urlpatterns = [
    path('', include(router.urls))
]