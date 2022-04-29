from django.urls import path
from rest_framework import routers

from .views import ArticleViewSet, CommentListAPIView, EntryViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('comments/', CommentListAPIView.as_view(), name="comment-list"),
]

urlpatterns += router.urls
