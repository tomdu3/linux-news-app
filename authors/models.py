from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('p_image', default='profile_image')

    def __str__(self):
        return f'Profile: {self.user.username}'