from django.db import models
from django.contrib.auth.models import User  # ← добавь импорт


class NewPost(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  # ← новое поле

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

