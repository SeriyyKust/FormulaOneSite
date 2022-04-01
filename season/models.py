from django.db import models
from django.urls import reverse


class Drivers(models.Model):
    name = models.CharField(max_length=100)
    fromCountry = models.CharField(max_length=50)
    wins = models.IntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    teams = models.ForeignKey('Teams', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'t_id': self.pk})


class Teams(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
