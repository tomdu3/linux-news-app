from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'slug', 'short_description', 'full_description', 'image_url', 'category']
