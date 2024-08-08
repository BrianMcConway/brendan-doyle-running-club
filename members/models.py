from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GPXFile(models.Model):
    title = models.CharField(max_length=255)
    file_data = models.BinaryField()  # Store file data as binary
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
