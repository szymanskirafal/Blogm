from rest_framework import routers

from .views import ArticleViewSet, EntryViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = router.urls
