from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'


# Book model
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField()
    image_url = CloudinaryField('image', default='default')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='book_details'
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_books',
        blank=True)
    # liked_by_user is a control field to check if the user has liked
    #  the book or not. It is not 'a strict field value' in the database
    liked_by_user = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def likes_counter(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}'
