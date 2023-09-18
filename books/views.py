from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from cloudinary import CloudinaryImage
from django.utils.text import slugify
from .models import Book, Category
from .forms import BookForm
from django.db.models import Q 
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
            'liked_by_user': liked_by_user,
             }
        return render(request, 'books/book_detail.html', context=context)


def user_favourites(request):
    user = request.user

    liked_books = Book.objects.filter(likes=user)
    context = {
        'user': user,
        'books': liked_books,
    }
    return render(request, 'books/user_favourites.html', context=context)


class BookUpdateView(LoginRequiredMixin, View):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        form = BookForm(instance=book)
        categories = Category.objects.all()

        context = {
            'book': book,
            'form': form,
            'categories': categories,
        }
        return render(request, 'books/book_edit.html', context)

    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        categories = Category.objects.all()
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_detail', book.slug)

        context = {
            'book': book,
            'form': form,
        }
        return render(request, 'books/book_edit.html', context)



class AddBookView(View):
    def get(self, request):
        form = BookForm()
        categories = Category.objects.all()

        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'books/book_add.html', context)

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user  # Get the current user

            # Extract cleaned data from the form
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            short_description = form.cleaned_data['short_description']
            full_description = form.cleaned_data['full_description']
            image_url = form.cleaned_data['image_url']
            category_name = form.cleaned_data['category']
            # Get the category instance based on the category name
            category = Category.objects.get(name=category_name)

            # Generate a slug based on the title
            base_slug = slugify(title)
            slug = base_slug
            counter = 1
            # Check if a record with the same slug already exists
            while Book.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            # Create and save the Book instance
            book = Book(
                title=title,
                author=author,
                short_description=short_description,
                full_description=full_description,
                image_url=image_url,
                category=category,
                slug=slug,
                user_id=user,
                status=1,
            )
            print(book.title, book.author, book.short_description, book.full_description, book.image_url, book.category, book.slug, book.user_id)

            book.save()

            return redirect('user_page')

        categories = Category.objects.all()

        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'books/book_add.html', context)

class BookDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        book.delete()
        return redirect('user_page')

def find_book(request):
    query = request.GET.get('q')
    if query:
        # Search for books that match the query in title or author
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        # If no query is provided, display all books
        books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/find_book.html', context=context)

def book_liked_by_user(book, user):
    return book.likes.filter(id=user.id).exists()


def like_book(request, slug):
    if request.method == 'POST' and request.user.is_authenticated:
        book = get_object_or_404(Book, slug=slug)
        
        # Check if the user has already liked the book
        liked_by_user = book.likes.filter(id=request.user.id).exists()
        
        if liked_by_user:
            # User has already liked the book, remove the like
            book.likes.remove(request.user)
        else:
            # User hasn't liked the book, add the like
            book.likes.add(request.user)
            
    # Redirect to the book detail page
    return redirect('book_detail', slug=slug)