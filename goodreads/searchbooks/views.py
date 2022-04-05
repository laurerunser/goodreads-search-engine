from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import SearchForm

from .models import Book

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def index(request):
    books = Book.objects.all()
    return render(request, 'search/index.html', {'books': books}, )


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    all_books = Book.objects.all()

    # get all the books descriptions
    all_descriptions = []
    for data in all_books:
        all_descriptions.append(data.description)

    # apply TFIDF on books
    vectorizer = TfidfVectorizer()
    matrix_tfidf = vectorizer.fit_transform(all_descriptions)

    # prep the reference book
    query_tfidf = vectorizer.transform([book.description])

    # # get the cosine distance and then keep the 20 best
    distances = cosine_similarity(query_tfidf, matrix_tfidf).flatten()
    best = np.argsort(distances)

    # get the books that correspond to the index we found
    recs = []
    for a in best:
        recs = [Book.objects.get(pk=a)] + recs

    # return the request
    c = {'book': book, 'recs': recs}
    return render(request, 'search/book_detail.html', c)


def search_page(request):
    return render(request, 'search/search_page.html')


def search_results(request):
    results = Book.objects.all()
    query = "TEST QUERY"
    c = {'search_string': query, 'results': results}
    return render(request, 'search/search_results.html', c)
