from django.db.models import Count

from rest_framework import permissions, viewsets

from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.annotate(number_of_comments=Count('comments'))
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', ]
