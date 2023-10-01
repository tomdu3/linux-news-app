from django import forms
from .models import Book


# Book form class
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'short_description', 'full_description', 'image_url', 'category']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # make image_url fields optional
        self.fields['image_url'].required = False