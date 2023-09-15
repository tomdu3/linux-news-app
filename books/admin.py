from django.contrib import admin
from .models import Book, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category)

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filters = ('status', 'created_on')
    summernote_fields = ('full_description',)