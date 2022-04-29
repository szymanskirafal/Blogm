from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets

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


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        query = Comment.objects.all()
        asset_category = self.request.query_params.get('asset_category')
        print('-------- asset category ', asset_category)
        # asset_pk = self.request.query_params.get('asset_pk')
        # print('-------- asset-pk ', asset_pk)
        model_dict = {
            'entry': 'entries',
            'article': 'articles',}
        app_name = model_dict.get(asset_category)
        if app_name is not None:
            asset_model = apps.get_model(app_label=app_name, model_name=asset_category)

            try:
                #asset_given = asset_model.objects.get(pk = asset_pk)
                asset_type = ContentType.objects.get_for_model(asset_model)
                print('------- asset_type is: ', asset_type)
                print('------- asset_type__pk is: ', asset_type.pk)
                query = Comment.objects.filter(content_type__pk = asset_type.id)

            except ObjectDoesNotExist:
                query = Comment.objects.all()
        return query
