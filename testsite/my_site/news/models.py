from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(
        max_length=130,
        verbose_name='Название новости',
        help_text='Не более 130-ти символов'
    )
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Загрузить фото')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    number_of_views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse_lazy('view-news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    category_title = models.CharField(max_length=130, db_index=True, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['category_title']
