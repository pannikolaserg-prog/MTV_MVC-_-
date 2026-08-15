from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    tags = models.JSONField(default=list, blank=True, verbose_name='Теги')
    is_public = models.BooleanField(default=False, verbose_name='Публичная')
    allow_comments = models.BooleanField(default=True, verbose_name='Разрешены комментарии')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    encrypted_note = models.BinaryField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Запись дневника'
        verbose_name_plural = 'Записи дневника'

    def __str__(self):
        return self.title

    def get_word_count(self):
        return len(self.content.split())
