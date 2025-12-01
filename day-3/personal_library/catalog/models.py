from django.db import models

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
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # foreign key shows what this belongs to
    slug = models.SlugField(unique=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


# migration - version history
# we can track changes to the structure of our database