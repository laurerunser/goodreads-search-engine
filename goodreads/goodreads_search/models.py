from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField
    title = models.CharField
    description = models.TextField
    link = models.URLField
    series = models.CharField
    cover_link = models.URLField
    author_name = models.CharField
    author_link = models.URLField
    date_published = models.DateField
    average_rating = models.PositiveIntegerField
    ratings_counts = models.IntegerField
    ratings_5_stars = models.IntegerField
    ratings_4_stars = models.IntegerField
    ratings_3_stars = models.IntegerField
    ratings_2_stars = models.IntegerField
    ratings_1_stars = models.IntegerField
    review_count = models.IntegerField
