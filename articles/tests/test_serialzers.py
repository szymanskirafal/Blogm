from articles.models import Article
from articles.serializers import ArticleSerializer

import pytest


@pytest.mark.django_db
def test_serializer_has_required_fields():
    article = Article.objects.create(
        title="some tilte",
        content="some content",
    )
    serializer = ArticleSerializer(instance=article)
    data = serializer.data
    assert set(data.keys()) == set(
        [
            "id",
            "title",
            "content",
            "number_of_comments",
        ]
    )
