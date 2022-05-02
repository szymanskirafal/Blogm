from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    number_of_comments = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "number_of_comments",
        ]
