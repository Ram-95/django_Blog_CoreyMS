from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # The CASCADE here means that when a user is deleted then the associated posts are also deleted. But
    # Not vice versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pics is the directory where the uploaded pics are stored to.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        # To resize the images and store.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)