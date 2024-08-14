from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class GPXFile(models.Model):
    """
    Model representing a GPX file uploaded by a user.
    """
    title = models.CharField(max_length=255)
    file_data = models.BinaryField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
