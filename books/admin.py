from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filters = ('status', 'created_on')
    summernote_fields = ('full_description',)