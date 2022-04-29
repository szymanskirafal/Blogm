from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from comments.models import Comment


class Article(models.Model):
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    comments = GenericRelation(Comment)

    def __str__(self):
        return f'Article - {self.title}'
