from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Category
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