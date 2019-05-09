from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add=True) #set to current date time on creation only
    date_posted = models.DateTimeField(default=timezone.now) #consider timezone #pass in function but dont execute
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, post is deleted as well

    def __str__(self):
        return self.title

    # Reverse - return full url to string
    # Redirect - redirect to specific route
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})