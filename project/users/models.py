from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # create one to one model relationship with existing User model
    # on_delete when User is deleted, profile is deleted
    # when profile deleted, User remains
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
