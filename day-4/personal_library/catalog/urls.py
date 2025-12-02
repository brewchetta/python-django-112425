from django.urls import path
from . import views

urlpatterns = [
    # BOOK PATHS
    path("", views.all_books, name="all_books"),
    path("books/<slug:slug>", views.show_book, name="show_book"),
    path("new-book/", views.new_book, name="new_book"),
    path("edit-book/<slug:slug>", views.edit_book, name="edit_book"),
    path("delete-book/<slug:slug>", views.delete_book, name="delete_book"),
    # AUTHOR PATHS
    path("authors/<int:id>", views.author_bio, name="author_bio"),
    path("authors/create", views.create_author, name="create_author"),
    path("authors/<int:id>/edit", views.edit_author, name="edit_author"),
    path("authors/<int:id>/delete", views.delete_author, name="delete_author"),

    # LIBRARIAN / USER PATHS
    path("signup", views.signup, name="signup"),
    path("create-librarian", views.create_librarian, name="create_librarian"),
    path("login-user", views.login_user, name="login_user"),
    path("logout-user", views.logout_user, name="logout_user")
]