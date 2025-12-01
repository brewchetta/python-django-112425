from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from django.http import Http404

def all_books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'catalog/all_books.html', context)

def show_book(request, slug):
    query_set = Book.objects.filter(slug=slug)
    book = get_object_or_404(query_set)
    context = {
        "book": book
    }
    return render(request, 'catalog/show_book.html', context)

def author_bio(request, id):
    try:
        author = Author.objects.get(pk=id)
        # pk stands for primary key a.k.a. id
        author_books = Book.objects.filter(author=author)
        context = {
            "author": author,
            "author_books": author_books
        }
        return render(request, "catalog/author_bio.html", context)
    except: # if the author doesnt exist do something else
        raise Http404("Author not found")