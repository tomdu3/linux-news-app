from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('p_image', default='profile_image')

    def __str__(self):
        return f'Profile: {self.user.username}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Category: {self.name}'


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField()
    image_url = CloudinaryField('image', default='book_image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='book_details'
    )
    likes = models.ManyToManyField(User, related_name='liked_books')
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def likes_counter(self):
        return self.likes.count()

    def __str__(self):
        return f'Book: {self.title}'
