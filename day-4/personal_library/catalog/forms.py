from django import forms
from .models import Book, Author, Librarian
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# book form inherits from ModelForm
class BookForm(forms.ModelForm):
    # the Meta class is essential for knowing what the model will be and what fields will be included in the form
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres']
        # we have excluded the slug field so it doesn't get included in the form

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'background']

# special sign up form inherits from special UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# instead of a model form we use a generic form here
class LoginForm(forms.Form):
    # this is a normal character field
    username = forms.CharField(max_length=100)
    # this is a character field that hides the password
    password = forms.CharField(widget=forms.PasswordInput)

class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['first_name', 'last_name']