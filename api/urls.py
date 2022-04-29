from rest_framework import routers

from .views import ArticleViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = router.urls
