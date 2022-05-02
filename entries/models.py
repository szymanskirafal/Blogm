from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from comments.models import Comment


class Entry(models.Model):
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return f"Entry - {self.title}"
