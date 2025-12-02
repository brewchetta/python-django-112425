from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from django.http import Http404
from .forms import BookForm

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
    

def slugify(unslugified_string):
    return unslugified_string.replace(" ", "-").lower()
    

def new_book(request):
    if request.method == 'GET':
        context = {
            "form": BookForm()
        }
        return render(request, 'catalog/book_form.html', context)
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            slug = slugify(form.cleaned_data['title'])
            new_book = form.save()
            new_book.slug = slug
            new_book.save()
            return redirect('all_books')
    else:
        raise Http404("View not found")
