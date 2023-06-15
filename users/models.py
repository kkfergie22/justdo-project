from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """User profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)

    def __str__(self):
        """Return user's username"""
        return self.user.username
