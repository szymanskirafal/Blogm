from django.urls import path
from rest_framework import routers

from .views import ArticleViewSet, CommentListCreateAPIView, EntryViewSet

router = routers.SimpleRouter()
router.register(r"articles", ArticleViewSet)
router.register(r"entries", EntryViewSet)

urlpatterns = router.urls

urlpatterns = [
    path("comments/", CommentListCreateAPIView.as_view(), name="comment-list"),
]

urlpatterns += router.urls
