from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import permissions, viewsets


class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
