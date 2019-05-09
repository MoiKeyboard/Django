from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # create one to one model relationship with existing User model
    # on_delete when User is deleted, profile is deleted
    # when profile deleted, User remains
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Modify profile image
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)