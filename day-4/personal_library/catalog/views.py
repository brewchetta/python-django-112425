from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from django.http import Http404
from .forms import BookForm, AuthorForm

# HELPER FUNCTION

def slugify(unslugified_string):
    return unslugified_string.replace(" ", "-").lower()


# BOOK VIEWS

def all_books(request):
    context = {
        # Book.objects is generally how we query for certain instances of books
        # the .all() means just get all of em
        "books": Book.objects.all()
    }
    return render(request, 'catalog/all_books.html', context)

def show_book(request, slug):
    # the .filter allows us to get specific books based on a filter argument
    # in this case we're filtering based on the slug that was put into the url
    query_set = Book.objects.filter(slug=slug)
    book = get_object_or_404(query_set)
    context = {
        "book": book
    }
    return render(request, 'catalog/show_book.html', context)
    

def new_book(request):
    if request.method == 'GET': # if we have get request show book form
        context = {
            # create a book form - BookForm() creates data for a form with all the inputs that a book would need to get created
            "form": BookForm()
        }
        return render(request, 'catalog/book_form.html', context)
    elif request.method == 'POST': # if we have a post request process the new book
        # create a new instance of the form - it has all the information from the post request so we can use it to build a new book
        form = BookForm(request.POST)
        # check to see if the form is valid
        if form.is_valid():
            # we get the title and slugify for later
            slug = slugify(form.cleaned_data['title'])
            # form.save() will insert the new book into the database
            new_book = form.save()
            new_book.slug = slug
            # if the book already exists, it will update the book instead
            new_book.save()
            return redirect('all_books')
    else:
        raise Http404("View not found")
    

def edit_book(request, slug):
    # the .filter allows us to find a book based on its slug
    query_set = Book.objects.filter(slug=slug)
    # get_object_or_404 does what it sounds like where it will either get the single book or else throw a 404 error
    book = get_object_or_404(query_set)
    if request.method == "GET": # if we get a GET request...
        context = {
            # important change from creating a book is we can fill the new form with the book to update's info
            "form": BookForm(instance=book),
            "book": book
        }
        return render(request, "catalog/edit_book.html", context)
    elif request.method == "POST":
        # when the book form is submitted we take the information from the POST and also link it to the particular book instance
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            slug = slugify(form.cleaned_data['title'])
            new_book = form.save()
            new_book.slug = slug
            new_book.save()
            return redirect('all_books')
        

def delete_book(request, slug):
    # find the book
    query_set = Book.objects.filter(slug=slug)
    book = get_object_or_404(query_set)
    # since the form is just a submit button no need to use the BookForm
    # just render the html
    if request.method == "GET":
        context = { "book": book }
        return render(request, "catalog/delete_book.html", context)
    elif request.method == "POST":
        # on the submission we just .delete and we're good to go
        book.delete()
        return redirect('all_books')
        # ^^^ importantly we redirect back to the index page instead of the book's page because the book no longer exists


# AUTHOR VIEWS

def author_bio(request, id):
    try:
        # the .get is great for finding based on an id
        # the .get will only get a single item
        # pk stands for primary key a.k.a. id
        author = Author.objects.get(pk=id)
        author_books = Book.objects.filter(author=author)
        context = {
            "author": author,
            "author_books": author_books
        }
        return render(request, "catalog/author_bio.html", context)
    except: # if the author doesnt exist do something else
        raise Http404("Author not found")
    

def create_author(request):
    if request.method == "GET":
        form = AuthorForm()
        context = { "form": form }
        return render(request, 'catalog/create_author.html', context)
    elif request.method == "POST":
        author = AuthorForm(request.POST)
        if author.is_valid():
            saved_author = author.save()
            return redirect('author_bio', saved_author.id)


def edit_author(request, id):
    author = Author.objects.get(pk=id)
    if request.method == "GET":
        form = AuthorForm(instance=author)
        context = { "form": form, "author": author }
        return render(request, "catalog/edit_author.html", context)
    elif request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_bio', author.id)
        

def delete_author(request, id):
    author = Author.objects.get(pk=id)
    if request.method == "GET":
        context = { "author": author }
        return render(request, "catalog/delete_author.html", context)
    elif request.method == "POST":
        author.delete()
        return redirect("all_books")

# CRUD - create read update delete