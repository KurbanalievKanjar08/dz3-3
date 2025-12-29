from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание', blank=True)
    publication_date = models.DateField(verbose_name='Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    
    def __str__(self):
        return f"{self.title} - {self.author}"
