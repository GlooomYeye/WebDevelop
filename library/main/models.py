from django.db import models

class Book(models.Model):
    name = models.CharField('Название книги', max_length=255)
    author = models.CharField('Автор', max_length=255)
    price = models.IntegerField('Цена')
    genre = models.CharField('Жанр', max_length=255)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'