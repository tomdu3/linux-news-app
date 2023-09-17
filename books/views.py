from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import Book, Category
from cloudinary import CloudinaryImage
# Create your views here.


def home(request):
    return render(request, 'books/home.html')

def user_page(request):
    user = request.user

    user_books = Book.objects.filter(user_id=user.id)
    context = {
        'user': user,
        'books': user_books,
    }
    return render(request, 'books/user_page.html', context=context)

class BookDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        
        liked_by_user = False
        if book.likes.filter(id=request.user.id).exists():
            liked_by_user = True
        
        context = {
            'book': book,
            'liked_by_user': liked_by_user, }
        return render(request, 'books/book_detail.html', context=context)

def user_favourites(request):
    user = request.user

    liked_books = Book.objects.filter(likes=user)
    context = {
        'user': user,
        'books': liked_books,
    }
    return render(request, 'books/user_favourites.html', context=context)