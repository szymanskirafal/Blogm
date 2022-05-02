from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    number_of_comments = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Entry
        fields = [
            "id",
            "title",
            "content",
            "number_of_comments",
        ]
