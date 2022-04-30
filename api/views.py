from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets

from utils import get_asset_model
from articles.models import Article
from articles.serializers import ArticleSerializer
from comments.models import Comment
from comments.serializers import CommentSerializer
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


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        query = Comment.objects.all()
        asset_category = self.request.query_params.get('asset_category')
        asset_pk = self.request.query_params.get('asset_pk')
        asset_model = get_asset_model(asset_category)

        if asset_model is not None:
            query = query.filter(
                Q(content_type = asset_model),
                Q(object_id = asset_pk),)

        return query
