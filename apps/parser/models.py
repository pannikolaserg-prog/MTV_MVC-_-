from django.db import models

class ParsedNews(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]
