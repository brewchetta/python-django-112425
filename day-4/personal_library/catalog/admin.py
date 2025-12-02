from django.contrib import admin

# import each model that you want available
from .models import Book, Author, Genre, Librarian

# create a valid login / superuser so you can access the admin panel
# python manage.py createsuperuser

# this will allow us to see the models in the admin portal
# localhost:8000/admin
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Librarian)