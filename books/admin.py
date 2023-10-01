from django.contrib import admin
from .models import Book, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category)

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'slug')
    summernote_fields = ('full_description',)
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'author']