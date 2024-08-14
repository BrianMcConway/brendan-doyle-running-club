from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Model representing a user profile.
    Each profile is linked to a single User object.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Profile object.
        Returns the username of the associated User.
        """
        return self.user.username
