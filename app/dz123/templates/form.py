from django import forms
from .models import Reader, Book

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['name', 'email', 'phone']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
