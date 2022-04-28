from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f'Entry - {self.title}'
