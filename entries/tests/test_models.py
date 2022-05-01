from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from entries.models import Entry

import pytest

class TestEntry:

    def test_title_field(self):
        field = Entry._meta.get_field('title')
        field_type_expected = models.CharField
        field_type_given = field.__class__
        assert field_type_expected == field_type_given
        field_max_length_expected = 150
        field_max_length_given = field.max_length
        assert field_max_length_expected == field_max_length_given
        field_unique_expected = True
        field_unique_given = field.unique
        assert field_unique_expected == field_unique_given

    def test_content_field(self):
        field = Entry._meta.get_field('content')
        field_type_expected = models.TextField
        field_type_given = field.__class__
        assert field_type_expected == field_type_given

    def test_comments_field(self):
        comment = Entry._meta.get_field('comments')
        assert GenericRelation == comment.__class__
