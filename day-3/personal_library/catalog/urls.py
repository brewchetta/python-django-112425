from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_books, name="all_books"),
    path("books/<slug:slug>", views.show_book, name="show_book"),
    path("authors/<int:id>", views.author_bio, name="author_bio")
]