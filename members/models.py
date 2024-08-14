from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class GPXFile(models.Model):
    title = models.CharField(max_length=255)
    file_data = models.BinaryField()  # Store file data as binary
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Change to auto_now_add

    def __str__(self):
        return self.title