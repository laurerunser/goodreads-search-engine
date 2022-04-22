import csv
from .models import Book # imports the model
with open('searchbooks/data/test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Book(id=row['id'], title=row['title'], description=row['description'], 
        link=row['link'], series=row['series'], cover_link=row['cover_link'], 
        author_name=row['author'], author_link=row['author_link'], date_published=row['date_published'], 
        average_rating=row['average_rating'], ratings_counts=row['rating_count'], 
        ratings_5_stars=row['five_star_ratings'], ratings_4_stars=row['four_star_ratings'], 
        ratings_3_stars=row['three_star_ratings'], ratings_2_stars=row['two_star_ratings'], 
        ratings_1_stars=row['one_star_ratings'], review_count=row['review_count'] )
        p.save()
