from entries.models import Entry
from entries.serializers import EntrySerializer

import pytest


@pytest.mark.django_db
def test_serializer_has_required_fields():
    entry = Entry.objects.create(
        title = 'some tilte',
        content = 'some content',)
    serializer = EntrySerializer(instance=entry)
    data = serializer.data
    assert set(data.keys()) == set(['id', 'title', 'content', 'number_of_comments', ])
