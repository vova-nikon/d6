from django import forms
from p_library.models import Author, Book, Reader

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReaderCreationForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name']