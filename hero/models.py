from django.db import models
from djongo.models.fields import ArrayField

# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Titles(models.Model):
    tconst = models.CharField(primary_key=True, max_length=500)
    titleType = models.CharField(max_length=500)
    primaryTitle = models.CharField(max_length=500)
    originalTitle = models.CharField(max_length=500)
    isAdult = models.BooleanField()
    startYear = models.CharField(max_length=4)
    endYear = models.CharField(max_length=4)
    runtimeMinutes = models.CharField(max_length=4)
    genres = models.JSONField()

    class Meta:
        db_table = 'titles'