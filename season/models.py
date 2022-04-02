from django.db import models
from django.urls import reverse


class Drivers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    fromCountry = models.CharField(max_length=50, verbose_name="Страна")
    wins = models.IntegerField(verbose_name="Количество подеб")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания статьи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время последнего обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    teams = models.ForeignKey('Teams', on_delete=models.PROTECT, null=True, verbose_name="Команда")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'t_id': self.pk})

    class Meta:
        verbose_name = "Гонщики"
        verbose_name_plural = "Гонщики"
        ordering = ['name', 'time_create']


class Teams(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Команда")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команды"
        verbose_name_plural = "Команды"
