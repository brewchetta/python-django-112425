from django import forms
from .models import Book, Author

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










    # LUNCH - RETURN AT 2:05 EST
    # LUNCH - RETURN AT 2:05 EST
        # LUNCH - RETURN AT 2:05 EST
            # LUNCH - RETURN AT 2:05 EST
                # LUNCH - RETURN AT 2:05 EST
                    # LUNCH - RETURN AT 2:05 EST
                        # LUNCH - RETURN AT 2:05 EST
                            # LUNCH - RETURN AT 2:05 EST
                                # LUNCH - RETURN AT 2:05 EST
                                    # LUNCH - RETURN AT 2:05 EST
                                        # LUNCH - RETURN AT 2:05 EST
                                            # LUNCH - RETURN AT 2:05 EST
                                                # LUNCH - RETURN AT 2:05 EST
                                                