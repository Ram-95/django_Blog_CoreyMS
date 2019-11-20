from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# This is a class that acts as a table to store the user posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # To print the title of the post when selecting
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})