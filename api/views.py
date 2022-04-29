from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from articles.models import Article
from articles.serializers import ArticleSerializer
from entries.models import Entry
from entries.serializers import EntrySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.annotate(number_of_comments=Count('comments'))
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', ]


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.annotate(number_of_comments=Count('comments'))
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['number_of_comments']
