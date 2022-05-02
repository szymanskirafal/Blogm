from django.db import models

from comments.models import Comment

import pytest


class TestComment:

    def test_body_field(self):
        field = Comment._meta.get_field('body')
        field_type_expected = models.CharField
        field_type_given = field.__class__
        assert field_type_expected == field_type_given
        field_max_length_expected = 300
        field_max_length_given = field.max_length
        assert field_max_length_expected == field_max_length_given
