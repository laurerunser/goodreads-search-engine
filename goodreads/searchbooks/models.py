from django.db import models

# Create your models here.
from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    link = models.URLField(null=True)
    series = models.CharField(max_length=200, null=True)
    cover_link = models.URLField(null=True)
    author_name = models.CharField(max_length=200, null=True)
    author_link = models.URLField(null=True)
    date_published = models.CharField(max_length=200, null=True)
    average_rating = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ratings_counts = models.IntegerField(null=True)
    ratings_5_stars = models.IntegerField(null=True)
    ratings_4_stars = models.IntegerField(null=True)
    ratings_3_stars = models.IntegerField(null=True)
    ratings_2_stars = models.IntegerField(null=True)
    ratings_1_stars = models.IntegerField(null=True)
    review_count = models.IntegerField(null=True)

    def __str(self):
        return self.id + " " + self.title + " - " + self.author_name
