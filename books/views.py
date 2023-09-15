from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'books/home.html')

def user_page(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'books/user_page.html', context=context)