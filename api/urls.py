from rest_framework import routers
from .views import ArticlesViewSet


router = routers.SimpleRouter()
router.register(r'articles', ArticlesViewSet)
urlpatterns = router.urls
