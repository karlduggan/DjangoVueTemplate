"""
Profile Model:
The profile model is used to store additional information about the users,
such as their personal details, preferences, or settings.
"""
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    # Add additional fields as per your requirements
    # ...

    def __str__(self):
        return self.user.username
