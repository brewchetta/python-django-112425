from django.db import models
from django.contrib.auth.models import User # special user model

# one to many - for example an author has many books
    # a book belongs to an author
    # foreign key - which points to the author it belongs to

# many to many - a genre can have many books and a book can have many genres
    # under the hood django creates a join table
    # frankenstein << join1 >> horror


class Author(models.Model):
    name = models.CharField(max_length=200)
    background = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model): # inheriting from the built in Model
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    # foreign key shows what this belongs to
    # foreign key references a different table (authors table)
    # on_delete determines what happens when the author gets deleted (delete all books here)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # many to many means a book can belong to many genres and a genre can have many books
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    

class Librarian(models.Model):
    # we get the user model from django's special auth module
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # directly links the librarian to the user
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # years_employed = models.IntegerField()
    # date_joined = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# migration - version history
# we can track changes to the structure of our database

# python manage.py makemigrations 

# ^^^ this will generate the migrations, kind of similar to git add
# you can see your migration history in the migrations folder

# when you have migrations ready you can run:

# python manage.py migrate

# this be what actually alters the db and creates the structure for the models, kind of similar to git commit

# after adding models it's STRONGLY recommended you also now add them to the admin.py