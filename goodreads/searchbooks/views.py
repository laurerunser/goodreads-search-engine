from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Book


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'search/book_detail.html', {'book': book})
