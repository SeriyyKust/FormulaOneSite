from django.db import models


class Drivers(models.Model):
    name = models.CharField(max_length=100)
    fromCountry = models.CharField(max_length=50)
    wins = models.IntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
