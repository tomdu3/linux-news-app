from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models


# User Profile Model - Extends the User Model with a profile image
class UserProfile(models.Model):
    ''' Update the user profile with a profile image'''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('Profile Image', default='profile_image')

    def __str__(self):
        return f'Profile: {self.user.username}'
