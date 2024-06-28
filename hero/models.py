from django.db import models
from djongo.models.fields import ArrayField

# Create your models here.

class Genres(models.Model):
    """
    Represents a genre of titles.

    Attributes:
    - `name` (models.CharField): The name of the genre.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        """
        Returns a string representation of the genre.
        """
        return self.name

    class Meta:
        abstract = True # Indicates that this model will not be used to create any database table.

class Titles(models.Model):
    """
    Represents the details of a title.

    Attributes:
    - `tconst` (models.CharField): The unique identifier for the title, also the primary key.
    - `titleType` (models.CharField): The type/category of the title.
    - `primaryTitle` (models.CharField): The primary name of the title.
    - `originalTitle` (models.CharField): The original name of the title.
    - `isAdult` (models.BooleanField): Indicates if the title is adult-rated.
    - `startYear` (models.CharField): The release or start year of the title.
    - `endYear` (models.CharField): The end year of the title's availability.
    - `runtimeMinutes` (models.CharField): The runtime of the title in minutes.
    - `genres` (models.JSONField): The genres associated with the title, stored in JSON format.
    """
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
        db_table = 'titles' # Defines the name of the table in the database.