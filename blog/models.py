from django.db import models
from django.urls import reverse
from datetime import date


class Article(models.Model):
    title = models.CharField(max_length=100, help_text="Введите название статьи")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, help_text="Выберите автора")
    date_of_writing = models.DateField(help_text="Выберите дату написания")
    description = models.CharField(max_length=300, help_text="Введите описание")
    text_of_article = models.TextField(help_text="Введите текст статьи", default="В процессе написания...")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Author(models.Model):
    nickname = models.CharField(max_length=30, help_text="Введите никнейм")
    date_of_birth = models.DateField(help_text="Введите дату рождения")

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])