from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'


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
    likes = models.ManyToManyField(User, related_name='liked_books', blank=True)
    liked_by_user = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def likes_counter(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}'
